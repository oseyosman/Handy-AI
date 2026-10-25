#!/usr/bin/env python3
"""
Gesture Mouse + Double-Clap YouTube launcher
============================================
Control the mouse with hand gestures (webcam + MediaPipe Hands).
Double-clap (microphone) opens YouTube at any time.

Works on macOS and Windows.

Keys (preview window must be focused):
    q / ESC  quit
    p        pause / resume hand control
    - / =    lower / raise the clap threshold
"""

from __future__ import annotations

import argparse
import math
import platform
import threading
import time
import webbrowser

import cv2
import mediapipe as mp
import numpy as np
import pyautogui

IS_WINDOWS = platform.system() == "Windows"
IS_MAC = platform.system() == "Darwin"

# ============================================================== tuning ======
MARGIN = 0.15            # unused border of the camera frame (cursor reaches screen edges)
PINCH_ON = 0.28          # pinch starts when thumb-tip distance / palm size < this
PINCH_OFF = 0.40         # pinch ends when it rises above this (hysteresis)
CONFIRM_FRAMES = 2       # frames a pinch must be seen before it counts
ARM_DELAY = 0.30         # seconds after REST/SCROLL/IDLE before clicks are accepted
DRAG_HOLD_S = 0.40       # index pinch held this long => drag instead of click
SCROLL_DEADZONE = 0.04   # fist must move this far (fraction of frame height) to scroll
SCROLL_GAIN = 25.0       # scroll speed (lines per frame at full offset)
SCROLL_UNIT = 40 if IS_WINDOWS else 1   # Windows wheel delta: 120 = 1 notch (3 lines)
OFFSET_DECAY = 0.92      # how fast the cursor re-syncs after an anchor change
LOST_GRACE_S = 0.40      # hand may vanish this long without releasing a drag
EXT_RATIO = 1.0          # finger counts as extended if tip is farther from wrist than PIP

CLAP_MIN_GAP = 0.12      # min seconds between the two claps
CLAP_MAX_GAP = 0.70      # max seconds between the two claps
CLAP_COOLDOWN = 3.0      # ignore audio this long after a double clap

# (tip, pip) landmark ids for index, middle, ring, pinky
FINGERS = ((8, 6), (12, 10), (16, 14), (20, 18))

WINDOW = "Gesture Mouse"
FONT = cv2.FONT_HERSHEY_SIMPLEX
MODE_COLORS = {
    "MOUSE": (0, 220, 0),
    "DRAG": (0, 165, 255),
    "SCROLL": (255, 200, 0),
    "REST": (180, 180, 180),
    "IDLE": (140, 140, 140),
    "PAUSED": (0, 0, 255),
    "NO HAND": (100, 100, 100),
}


def dist(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.norm(a - b))


# ============================================================ clap detector ==
class ClapDetector:
    """Detects two sharp audio peaks in quick succession."""

    def __init__(self, threshold: float):
        self.threshold = threshold
        self.level = 0.0            # decaying peak level for the UI (0..1)
        self.available = False
        self._stream = None
        self._armed = True
        self._first: float | None = None
        self._last_spike = 0.0
        self._cooldown_until = 0.0
        self._event = threading.Event()

    def start(self) -> None:
        try:
            import sounddevice as sd

            info = sd.query_devices(kind="input")
            rate = int(info["default_samplerate"])
            self._stream = sd.InputStream(
                channels=1,
                samplerate=rate,
                blocksize=int(rate * 0.02),   # ~20 ms blocks
                dtype="float32",
                callback=self._callback,
            )
            self._stream.start()
            self.available = True
        except Exception as exc:  # no mic, no permission, no PortAudio...
            print(f"[clap] microphone unavailable, clap detection off: {exc}")

    def stop(self) -> None:
        if self._stream is not None:
            try:
                self._stream.stop()
                self._stream.close()
            except Exception:
                pass

    def consume(self) -> bool:
        if self._event.is_set():
            self._event.clear()
            return True
        return False

    def _callback(self, indata, frames, time_info, status) -> None:  # audio thread
        peak = float(np.abs(indata).max())
        self.level = max(peak, self.level * 0.88)
        now = time.monotonic()
        if now < self._cooldown_until:
            return
        if self._armed:
            if peak >= self.threshold:                     # rising edge = one clap
                self._armed = False
                self._last_spike = now
                if self._first is not None and now - self._first <= CLAP_MAX_GAP:
                    self._first = None
                    self._cooldown_until = now + CLAP_COOLDOWN
                    self._event.set()
                else:
                    self._first = now
        elif peak < self.threshold * 0.5 and now - self._last_spike >= CLAP_MIN_GAP:
            self._armed = True


# ======================================================== gesture controller ==
class GestureController:
    """Turns hand landmarks (pixel coords) into mouse actions."""

    def __init__(self, screen_w: int, screen_h: int):
        self.sw, self.sh = screen_w, screen_h
        self.cursor: np.ndarray | None = None
        self.offset = np.zeros(2)
        self.anchor_kind: str | None = None

        self.pinch: str | None = None       # "index" | "middle" | "ring"
        self.pinch_t0 = 0.0
        self.dragging = False
        self._pending: str | None = None
        self._pending_n = 0

        self.scroll_anchor: float | None = None
        self.scroll_acc = 0.0

        self.last_idle = time.monotonic()
        self.last_seen = time.monotonic()

    # ---- public ------------------------------------------------------------
    def update(self, pts: np.ndarray, w: int, h: int, now: float) -> str:
        self.last_seen = now
        size = max(dist(pts[0], pts[9]), 1e-6)       # palm length = scale reference
        ext = [dist(pts[0], pts[t]) > dist(pts[0], pts[p]) * EXT_RATIO for t, p in FINGERS]
        thumb = pts[4]
        dists = {
            "index": dist(thumb, pts[8]) / size,
            "middle": dist(thumb, pts[12]) / size,
            "ring": dist(thumb, pts[16]) / size,
        }

        # Fist -> scroll
        if not any(ext):
            self._cancel_pinch()
            return self._scroll(pts, h, now)
        self.scroll_anchor = None

        # Pinch gestures
        active = self._update_pinch(dists, ext, now)
        if active is not None:
            if active == "index":
                if not self.dragging and now - self.pinch_t0 >= DRAG_HOLD_S:
                    pyautogui.mouseDown(button="left", _pause=False)
                    self.dragging = True
                    self.anchor_kind = None          # rebase cursor onto pinch point
                if self.dragging:
                    mid = (pts[4] + pts[8]) / 2
                    self._move_cursor(mid, w, h, "pinch", dragging=True)
                    return "DRAG"
            return "MOUSE"                           # cursor frozen while pinching

        # Open palm -> rest
        if all(ext):
            self._mark_idle(now)
            return "REST"

        # Index finger pointing -> move cursor
        if ext[0] and not ext[1] and not ext[2]:
            self._move_cursor(pts[8], w, h, "tip")
            return "MOUSE"

        self.last_idle = now
        return "IDLE"

    def lost(self, now: float) -> str:
        if now - self.last_seen > LOST_GRACE_S:
            self.reset(now)
        return "NO HAND"

    def reset(self, now: float | None = None) -> None:
        self._cancel_pinch()
        self.scroll_anchor = None
        self.cursor = None
        self.anchor_kind = None
        self.last_idle = time.monotonic() if now is None else now

    # ---- pinch handling ----------------------------------------------------
    def _update_pinch(self, dists, ext, now) -> str | None:
        if self.pinch is not None:                    # already pinching: wait for release
            if dists[self.pinch] < PINCH_OFF:
                return self.pinch
            self._end_pinch()
            return None

        cand = None
        for name, i in (("index", 0), ("middle", 1), ("ring", 2)):
            # valid pinch = that finger meets the thumb while the other 3 stay extended
            if dists[name] < PINCH_ON and all(ext[j] for j in range(4) if j != i):
                if cand is None or dists[name] < dists[cand]:
                    cand = name

        if cand is not None and now - self.last_idle > ARM_DELAY:
            if cand == self._pending:
                self._pending_n += 1
            else:
                self._pending, self._pending_n = cand, 1
            if self._pending_n >= CONFIRM_FRAMES:
                self._start_pinch(cand, now)
                return cand
        else:
            self._pending, self._pending_n = None, 0
        return None

    def _start_pinch(self, name: str, now: float) -> None:
        self.pinch = name
        self.pinch_t0 = now
        self.dragging = False
        self._pending, self._pending_n = None, 0
        self.anchor_kind = None                       # freeze cursor
        if name == "middle":
            pyautogui.doubleClick(_pause=False)
        elif name == "ring":
            pyautogui.rightClick(_pause=False)

    def _end_pinch(self) -> None:
        if self.pinch == "index":
            if self.dragging:
                pyautogui.mouseUp(button="left", _pause=False)
            else:
                pyautogui.click(_pause=False)         # short pinch = left click
        self.pinch = None
        self.dragging = False
        self.anchor_kind = None

    def _cancel_pinch(self) -> None:
        if self.dragging:
            pyautogui.mouseUp(button="left", _pause=False)
        self.pinch = None
        self.dragging = False
        self._pending, self._pending_n = None, 0

    # ---- scroll ------------------------------------------------------------
    def _scroll(self, pts: np.ndarray, h: int, now: float) -> str:
        self.last_idle = now
        y = float(pts[9][1]) / h
        if self.scroll_anchor is None:
            self.scroll_anchor = y
            self.scroll_acc = 0.0
        off = self.scroll_anchor - y                  # >0 when the hand moves up
        if abs(off) > SCROLL_DEADZONE:
            self.scroll_acc += math.copysign(abs(off) - SCROLL_DEADZONE, off) * SCROLL_GAIN
            lines = int(self.scroll_acc)
            if lines:
                pyautogui.scroll(lines * SCROLL_UNIT, _pause=False)
                self.scroll_acc -= lines
        else:
            self.scroll_acc = 0.0
        return "SCROLL"

    # ---- cursor ------------------------------------------------------------
    def _mark_idle(self, now: float) -> None:
        self._cancel_pinch()
        self.cursor = None                            # re-read real cursor next time
        self.anchor_kind = None
        self.last_idle = now

    def _move_cursor(self, anchor: np.ndarray, w: int, h: int, kind: str, dragging: bool = False) -> None:
        nx = (anchor[0] / w - MARGIN) / (1 - 2 * MARGIN)
        ny = (anchor[1] / h - MARGIN) / (1 - 2 * MARGIN)
        target = np.array([nx * (self.sw - 1), ny * (self.sh - 1)])

        if self.cursor is None:
            self.cursor = np.array(pyautogui.position(), dtype=float)
        if self.anchor_kind != kind:                  # avoid a jump when the anchor changes
            self.offset = self.cursor - target
            self.anchor_kind = kind
        self.offset *= OFFSET_DECAY

        target = np.clip(target + self.offset, 0, [self.sw - 1, self.sh - 1])
        delta = target - self.cursor
        d = float(np.hypot(*delta))
        if d < 1.5:                                   # ignore sub-pixel jitter
            return
        alpha = 0.25 + 0.65 * min(d / 250.0, 1.0)     # slow = smooth, fast = responsive
        self.cursor += delta * alpha
        x, y = int(round(self.cursor[0])), int(round(self.cursor[1]))
        if dragging:
            pyautogui.dragTo(x, y, button="left", mouseDownUp=False, _pause=False)
        else:
            pyautogui.moveTo(x, y, _pause=False)


# ================================================================ UI / main ==
def draw_hud(frame, mode, clap: ClapDetector, now, flash_until, hand_pt) -> None:
    h, w = frame.shape[:2]
    x0, y0 = int(w * MARGIN), int(h * MARGIN)
    cv2.rectangle(frame, (x0, y0), (w - x0, h - y0), (255, 128, 0), 1)

    color = MODE_COLORS.get(mode, (200, 200, 200))
    cv2.putText(frame, f"MODE: {mode}", (10, 28), FONT, 0.8, color, 2, cv2.LINE_AA)
    if hand_pt is not None:
        cv2.circle(frame, (int(hand_pt[0]), int(hand_pt[1])), 10, color, 2)

    bx, by, bw, bh = 10, h - 32, 200, 14
    if clap.available:
        cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (50, 50, 50), -1)
        fill = int(bw * min(clap.level, 1.0))
        bar = (0, 0, 255) if clap.level >= clap.threshold else (0, 200, 0)
        cv2.rectangle(frame, (bx, by), (bx + fill, by + bh), bar, -1)
        tx = bx + int(bw * min(clap.threshold, 1.0))
        cv2.line(frame, (tx, by - 4), (tx, by + bh + 4), (255, 255, 255), 2)
        cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (200, 200, 200), 1)
        cv2.putText(frame, f"MIC  thr {clap.threshold:.2f}", (bx + bw + 10, by + 12),
                    FONT, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    else:
        cv2.putText(frame, "MIC: off", (bx, by + 12), FONT, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    if now < flash_until:
        text = "CLAP!"
        (tw, th), _ = cv2.getTextSize(text, FONT, 3.0, 6)
        cv2.putText(frame, text, ((w - tw) // 2, (h + th) // 2), FONT, 3.0, (0, 255, 255), 6, cv2.LINE_AA)

    cv2.putText(frame, "q quit | p pause | -/= clap threshold", (10, h - 40),
                FONT, 0.4, (200, 200, 200), 1, cv2.LINE_AA)


def open_camera(index: int) -> cv2.VideoCapture:
    backend = cv2.CAP_DSHOW if IS_WINDOWS else cv2.CAP_ANY
    cap = cv2.VideoCapture(index, backend)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    return cap


def run_check(args) -> int:
    """Verify screen, camera and microphone, then exit."""
    print(f"Python {platform.python_version()} on {platform.system()} {platform.release()}")
    sw, sh = pyautogui.size()
    print(f"[ok] screen: {sw}x{sh}")

    cap = open_camera(args.camera)
    ok, frame = cap.read()
    cap.release()
    if ok:
        print(f"[ok] camera {args.camera}: frame {frame.shape[1]}x{frame.shape[0]}")
    else:
        print(f"[FAIL] camera {args.camera}: cannot read a frame (permission? wrong --camera index?)")

    try:
        import sounddevice as sd

        dev = sd.query_devices(kind="input")
        print(f"[ok] microphone: {dev['name']} @ {int(dev['default_samplerate'])} Hz")
    except Exception as exc:
        print(f"[FAIL] microphone: {exc}")
    return 0 if ok else 1


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Hand-gesture mouse + double-clap YouTube launcher")
    p.add_argument("--camera", type=int, default=0, help="camera index (default 0)")
    p.add_argument("--clap-threshold", type=float, default=0.30,
                   help="clap peak level 0..1 (default 0.30; tune with - and = keys)")
    p.add_argument("--url", default="https://www.youtube.com", help="page opened on double clap")
    p.add_argument("--no-clap", action="store_true", help="disable microphone / clap detection")
    p.add_argument("--check", action="store_true", help="test screen, camera, mic and exit")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    pyautogui.FAILSAFE = False     # cursor legitimately reaches screen corners; use 'q' to quit
    pyautogui.PAUSE = 0
    if hasattr(pyautogui, "MINIMUM_DURATION"):
        pyautogui.MINIMUM_DURATION = 0

    if args.check:
        return run_check(args)

    screen_w, screen_h = pyautogui.size()
    cap = open_camera(args.camera)
    if not cap.isOpened():
        print("Cannot open camera. Run with --check, grant camera permission, or try --camera 1.")
        return 1

    clap = ClapDetector(args.clap_threshold)
    if not args.no_clap:
        clap.start()

    ctrl = GestureController(screen_w, screen_h)
    hands = mp.solutions.hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        model_complexity=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.6,
    )
    drawer = mp.solutions.drawing_utils

    paused = False
    flash_until = 0.0
    print("Running. Focus the preview window; press q to quit, p to pause.")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Camera frame read failed.")
                break
            frame = cv2.flip(frame, 1)                     # mirror view
            h, w = frame.shape[:2]
            now = time.monotonic()

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb.flags.writeable = False
            result = hands.process(rgb)

            mode, hand_pt = "NO HAND", None
            if result.multi_hand_landmarks:
                lms = result.multi_hand_landmarks[0]
                drawer.draw_landmarks(frame, lms, mp.solutions.hands.HAND_CONNECTIONS)
                pts = np.array([(p.x * w, p.y * h) for p in lms.landmark])
                hand_pt = pts[8]
                if paused:
                    ctrl.reset(now)
                    mode = "PAUSED"
                else:
                    mode = ctrl.update(pts, w, h, now)
            else:
                mode = "PAUSED" if paused else ctrl.lost(now)

            if clap.consume():
                print("Double clap detected -> opening", args.url)
                webbrowser.open(args.url)
                flash_until = now + 1.0

            draw_hud(frame, mode, clap, now, flash_until, hand_pt)
            cv2.imshow(WINDOW, frame)

            key = cv2.waitKey(1) & 0xFF
            if key in (27, ord("q")):
                break
            elif key == ord("p"):
                paused = not paused
                ctrl.reset(now)
            elif key in (ord("="), ord("+")):
                clap.threshold = min(0.95, clap.threshold + 0.05)
            elif key in (ord("-"), ord("_")):
                clap.threshold = max(0.05, clap.threshold - 0.05)
    except KeyboardInterrupt:
        pass
    finally:
        ctrl.reset()
        clap.stop()
        hands.close()
        cap.release()
        cv2.destroyAllWindows()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())