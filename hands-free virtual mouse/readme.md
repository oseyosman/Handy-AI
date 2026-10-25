# Gesture Mouse + Double-Clap YouTube

Control your computer's mouse with hand gestures from your webcam (MediaPipe Hands).
Double-clap at any time to open YouTube. Works on **macOS** and **Windows**.

- Real-time microphone level bar in the preview window
- Big "CLAP!" flash when a double clap is detected
- Mode display: MOUSE / DRAG / SCROLL / REST / PAUSED

## Gestures

| Gesture | Mode | Action |
|---|---|---|
| Index finger up (other fingers curled) | MOUSE | Move cursor |
| Thumb + index pinch (other 3 fingers extended) | MOUSE | Left click |
| Thumb + middle pinch (other 3 extended) | MOUSE | Double click |
| Thumb + ring pinch (other 3 extended) | MOUSE | Right click |
| Thumb + index pinch, **hold ~0.4 s** | DRAG | Drag & drop (release to drop) |
| Fist, then move up / down | SCROLL | Scroll (further from start = faster) |
| Open palm | REST | No action (safe pose) |
| Double clap | always on | Opens YouTube |

Tips: the cursor freezes while you pinch so clicks land where you aim.
Go through REST (open palm) between actions if clicks misfire.
The blue rectangle in the preview is the active area; the cursor reaches the screen edges inside it.

## Setup

Python 3.10 - 3.12 is recommended (MediaPipe wheels).

### macOS (Terminal)

```bash
cd gesture-mouse
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Verify the install:

```bash
python -c "import mediapipe, cv2, pyautogui, sounddevice; print('imports ok')"
```

Grant permissions to your terminal app (Terminal, iTerm, or VS Code) in
**System Settings > Privacy & Security**:

1. **Camera**
2. **Microphone**
3. **Accessibility** (required to move/click the mouse)

Then quit and reopen the terminal, and verify hardware:

```bash
python main.py --check
```

### Windows (PowerShell)

```powershell
cd gesture-mouse
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If activation is blocked: `Set-ExecutionPolicy -Scope Process Bypass`, then activate again.

Verify the install:

```powershell
python -c "import mediapipe, cv2, pyautogui, sounddevice; print('imports ok')"
```

Make sure **Settings > Privacy & security > Camera / Microphone** allow desktop apps, then:

```powershell
python main.py --check
```

## Run

```bash
python main.py
```

Expected: a preview window opens showing the mirrored camera feed, a mode label, and a mic bar.
Raise one finger and the cursor should follow it.

Keys (preview window focused): `q` / `Esc` quit, `p` pause/resume hand control,
`-` / `=` lower/raise the clap threshold.

Options:

```text
--camera N            camera index (default 0)
--clap-threshold X    clap peak level 0..1 (default 0.30)
--url URL             page to open on double clap (default YouTube)
--no-clap             disable the microphone entirely
--check               test screen, camera, mic, then exit
```

## Tuning the clap detector

The white line on the mic bar is the threshold. A clap should push the bar past it (it turns red);
normal speech and typing should stay below it.

- Claps not detected: press `-` to lower the threshold (or raise your mic input volume).
- Speech or noise triggers it: press `=` to raise the threshold.
- Clap twice quickly (about 0.15 - 0.7 s apart). After a trigger it ignores audio for 3 s.

## Troubleshooting

| Problem | Fix |
|---|---|
| Camera won't open | Try `--camera 1`; close other apps using the camera; check permissions |
| macOS: mouse doesn't move or click | Add your terminal to **Accessibility**, then restart the terminal |
| macOS: black camera image | Add your terminal to **Camera**, then restart the terminal |
| Cursor jitters | Improve lighting; keep your hand 40 - 80 cm from the camera; raise `OFFSET_DECAY`/lower `alpha` in `main.py` |
| Clicks misfire | Raise `ARM_DELAY` or lower `PINCH_ON` at the top of `main.py` |
| Scroll too fast/slow | Change `SCROLL_GAIN` at the top of `main.py` |
| `pip install mediapipe` fails | Use Python 3.10 - 3.12 (not 3.13+) |

All tunables are constants at the top of `main.py`.

## Safety

The app controls your real mouse. Keep the preview window reachable so you can press `q` or `p`,
or press `Ctrl+C` in the terminal. The PyAutoGUI corner fail-safe is disabled because the cursor
legitimately reaches screen corners.

## Files

- `main.py` - the whole app (gesture controller, clap detector, preview UI)
- `requirements.txt` - dependencies
- `README.md` - this file