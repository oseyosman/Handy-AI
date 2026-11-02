<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%20--%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10-3.12"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/MediaPipe-Hands-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe"/>
  <img src="https://img.shields.io/badge/PyAutoGUI-OS%20Automation-E95420?style=for-the-badge" alt="PyAutoGUI"/>
  <img src="https://img.shields.io/badge/SoundDevice-Acoustic%20IO-009688?style=for-the-badge" alt="SoundDevice"/>
  <img src="https://img.shields.io/badge/Vanilla-HTML%2FCSS%2FJS-f7df1e?style=for-the-badge&logo=javascript&logoColor=black" alt="Vanilla JS"/>
  <img src="https://img.shields.io/badge/Web%20Audio-API-ff6bca?style=for-the-badge" alt="Web Audio"/>
  <img src="https://img.shields.io/badge/Zero-Dependencies-7cffc4?style=for-the-badge" alt="Zero Dependencies"/>
</p>

<h1 align="center">
  🖐️ Handy AI
</h1>

<p align="center">
  <strong>Gesture Intelligence, Hands-Free Virtual Mouse & Interactive Physics Suite</strong><br/>
  <sub>Real-time hand tracking · Desktop OS virtual mouse · Acoustic double-clap launcher · Fluid particle dynamics · Mid-air drawing</sub>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-the-suite">The Suite</a> •
  <a href="#-features">Features</a> •
  <a href="#-hands-free-virtual-mouse-desktop">Virtual Mouse</a> •
  <a href="#-handy-ai-flagship-web">Handy AI Core</a> •
  <a href="#-digital-playground-web">Digital Playground</a> •
  <a href="#-gestures-reference">Gestures</a> •
  <a href="#%EF%B8%8F-tech-stack">Tech Stack</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-troubleshooting">Troubleshooting</a> •
  <a href="#-credits">Credits</a>
</p>

---

## ✨ Overview

**Handy AI** is a complete computer vision and human-computer interaction (HCI) ecosystem powered by [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html). It bridges real-time webcam hand tracking with both **operating system-level desktop automation** and **zero-install browser-native creative computing**:

1. **Desktop System Controller** ([`hands-free virtual mouse`](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/hands-free%20virtual%20mouse/main.py)): Control your actual macOS or Windows mouse pointer with finger pointing, execute clicks and drag-and-drops with natural pinches, scroll with intuitive fist movements, and trigger web navigation (such as launching YouTube) with acoustic **double-clap detection** from your microphone.
2. **Flagship Gesture Web Suite** ([`index.html`](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/index.html)): Experience mid-air Bézier drawing, dual-hand geometry synthesizers, proximity-modulated spatial Web Audio, and Matrix rain visualizers with zero build tools and zero npm dependencies.
3. **Elemental Particle Laboratories** ([`digital_playground.html`](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/digital_playground.html) & [`playground .html`](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/playground%20.html)): Manipulate 6 reactive fluid materials (Water, Fire, Smoke, Sparks, Plasma, and Gravity singularities) with 7 distinct webcam poses, augmented reality bone skeletons, and dynamic force fields.

---

## 🚀 Quick Start

### 1. Hands-Free Virtual Mouse (Desktop App)

Operate your operating system's cursor and double-clap to open YouTube:

#### macOS Setup
```bash
# Navigate to the virtual mouse directory
cd "hands-free virtual mouse"

# Create and activate a Python 3.10-3.12 virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Verify your hardware (Camera, Microphone, Screen)
python main.py --check

# Start hands-free mouse control
python main.py
```

> [!IMPORTANT]
> **macOS Permissions Required**: Grant **Camera**, **Microphone**, and **Accessibility** (needed to move the mouse) permissions to your terminal app (Terminal, iTerm2, or VS Code) in **System Settings > Privacy & Security**, then restart your terminal.

#### Windows Setup (PowerShell)
```powershell
cd "hands-free virtual mouse"
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Verify hardware & start
python main.py --check
python main.py
```

---

### 2. Interactive Web Suite (Browser-Native)

Run the creative physics and gesture platforms directly in your browser:

```bash
# Serve the repository locally (required for camera permissions)
python3 -m http.server 8080
```

Open in **Google Chrome** or **Microsoft Edge**:
- 🖐️ **Handy AI Core**: [http://localhost:8080/index.html](http://localhost:8080/index.html)
- 🧪 **Digital Playground Pro**: [http://localhost:8080/digital_playground.html](http://localhost:8080/digital_playground.html)
- ⚡ **Particle Lab Lite**: [http://localhost:8080/playground%20.html](http://localhost:8080/playground%20.html)

---

## 📦 The Suite

| Application | Technology | Primary Role | Interaction Methods | Key Capabilities |
|:---|:---|:---|:---|:---|
| **Hands-Free Virtual Mouse** | Python 3, OpenCV, PyAutoGUI, SoundDevice | OS Desktop Mouse & Audio Trigger | Point, Pinches, Fist, Rest Palm, Double Clap | Full OS cursor movement, left/double/right click, drag & drop, scroll wheel, acoustic YouTube launcher |
| **Handy AI Core** | Vanilla HTML5/Canvas, Web Audio, MediaPipe JS | Gesture Intelligence & Spatial Audio | Dual-hand tracking, pinch triggers, pose recognition | 3 Modes (Play, Shapes, Write), algorithmic audio synthesis, Bézier air drawing, matrix rain |
| **Digital Playground (Pro)** | HTML5 Canvas, Euler Particle Engine, MediaPipe JS | Elemental Fluid & Force Field Lab | 7 AI webcam gestures, mouse drag, touch | 6 elemental materials, live AR skeleton overlay with wrist name tags, neon gesture badge, force fields |
| **Particle Lab (Lite)** | Lightweight Canvas 2D, MediaPipe JS | Fast-loading interactive physics | Index-finger pointing, pinch clutch | Streamlined sandbox, instant launch, turbulence & gravity toggles, responsive force brushes |

---

## 🎯 Features

### 🖱️ Desktop Virtual Mouse & Acoustic Automation
- **Smooth System Cursor Control**: Maps webcam index-finger tracking into native OS screen coordinates with exponential smoothing (EMA) and active-area margin calibration.
- **Freeze-on-Pinch Aiming**: Cursor automatically freezes during pinch initialization so clicks land precisely where aimed without drift.
- **Natural Pinch Gestures**:
  - Thumb + Index: Instantaneous Left Click
  - Thumb + Index (Held > 0.4s): Drag & Drop mode
  - Thumb + Middle: Double Click
  - Thumb + Ring: Right Click (Context Menu)
- **Fist Velocity Scrolling**: Clenching into a fist anchors a scroll position; moving vertically scrolls up or down with proportional acceleration.
- **REST Safe Pose**: Spread open palm safely neutralizes cursor actions to prevent accidental misclicks.
- **Acoustic Double-Clap Detection**: Background microphone thread performs real-time audio peak detection. Two sharp claps within 0.12s–0.70s flash a glowing "CLAP!" HUD alert and instantly open YouTube (or a custom URL).

### 🖐️ Computer Vision & Tracking Engine
- **MediaPipe Hands Integration**: Real-time 21-landmark 3D coordinate detection running client-side at up to 60 FPS.
- **Single & Dual Hand Detection**: Supports two-handed interactions, inter-hand proximity hum, and multi-hand shape formation.
- **AR Skeleton & HUD Overlays**: Luminous dual-layer bones, energy crowns, live gesture name tags anchored to the wrist, and neon gesture status badges.
- **Gesture Hysteresis & Temporal Filtering**: Multi-frame temporal stability filtering to eliminate flickering gesture states, with exponential moving average (EMA) smoothing on coordinates.

### 🌊 Physics & Particle Simulation
- **6 Reactive Elements**:
  - 💧 **Water**: Fluid cohesion, smooth gravitational drift, and aqua hues.
  - 🔥 **Fire**: Upward buoyant rise, thermal turbulence, and blazing yellow-orange fade.
  - ☁️ **Smoke**: Soft billows, gentle air drag, and atmospheric expansion.
  - ✨ **Sparks**: High-velocity explosive dispersal with short energetic lifespans.
  - 🫧 **Plasma**: Neon violet charge particles with erratic high-energy velocities.
  - 🌀 **Gravity**: Deep space gravitational singularities pulling nearby matter.
- **Force Field System**: Switch between **Paint**, **Attract** (gravitational pull), **Repel** (deflection shield), and **Nova Burst** (radial shockwaves).
- **Environmental Controls**: Toggle gravity, fluid turbulence, and particle trails; fine-tune brush size, emission rate, force multiplier, and particle lifetime in real time.

### 🎨 Creative Canvas & Audio
- **Air Drawing**: Point your index finger to sketch in 3D space with quadratic Bézier curve smoothing and hue-cycling palettes.
- **Spatial Web Audio API**: Procedural sound generation without audio assets — sawtooth zaps, sine pops, and continuous two-hand proximity frequency modulation (80–360 Hz).
- **Atmospheric Visuals**: Katakana Matrix rain reacting to hand velocity, SVG fractal noise grain overlay, and glassmorphic HUD controls.

---

## 🖱️ Hands-Free Virtual Mouse (Desktop)

Located in [`hands-free virtual mouse/main.py`](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/hands-free%20virtual%20mouse/main.py).

### Gesture Controls
| Gesture | Pose | Operating Mode | System Action |
|:---|:---|:---|:---|
| ☝️ **Point** | Index extended, others curled | `MOUSE` | Moves the system mouse cursor smoothly |
| 🤏 **Index Pinch** | Thumb + Index pinched (<0.4s) | `MOUSE` | **Left Click** (cursor freezes for accuracy) |
| ✊ **Index Pinch Hold** | Thumb + Index held (>0.4s) | `DRAG` | **Drag & Drop** (drags until pinch is released) |
| ✌️ **Middle Pinch** | Thumb + Middle pinched | `MOUSE` | **Double Click** |
| 💍 **Ring Pinch** | Thumb + Ring pinched | `MOUSE` | **Right Click** (Context Menu) |
| ✊ **Fist Move** | Clenched fist moved up / down | `SCROLL` | **Scroll Wheel** (distance from start controls speed) |
| ✋ **Open Palm** | All fingers spread wide | `REST` | **Safe Pose** (no mouse movement or click triggers) |
| 👏 **Double Clap** | Two rapid claps (0.12–0.70s) | *Always Active* | Flashes HUD banner & **Opens YouTube** in default browser |

### Preview HUD & Keyboard Shortcuts
When the OpenCV preview window is focused:
- **Active Area (Blue Rectangle)**: Maps the comfortable inner 70% of the camera frame to 100% of your screen resolution, letting you reach edges easily.
- **Audio Meter Bar**: Live microphone level display. The white tick marks the clap trigger threshold; passing it turns the bar red.
- **Keyboard Shortcuts**:
  - `q` or `Esc` : Exit and quit application
  - `p` : Pause / resume hand tracking
  - `-` / `=` : Lower / raise clap detection sensitivity threshold

### Command-Line Arguments
```bash
python main.py [options]

Options:
  --camera N            Camera index (default: 0)
  --clap-threshold X    Clap peak sensitivity level 0.0 to 1.0 (default: 0.30)
  --url URL             Target URL to launch on double clap (default: YouTube)
  --no-clap             Disable microphone and acoustic detection entirely
  --check               Run diagnostic check on camera, mic, and screen, then exit
```

---

## 🎮 Handy AI Flagship (`index.html`)

Located in [`index.html`](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/index.html).

### ▶ Play Mode — `#7cffc4`
The default sensory playground. Your hands become color-shifting energy skeletons with sparkling particle trails emitting from each fingertip:
- **Pinch** thumb + index: Triggers an electric ⚡ zap sound with expanding dual-ring ripples and particle bursts.
- **Two hands**: Gradient laser lines bridge matching fingertips across both hands.
- **Close fingertips (<140px)**: Jagged procedural lightning arcs between fingertips.
- **Wireframe Mandala**: A rotating geometric pattern forms at the centroid of all 10 fingertips.
- **Proximity Hum**: Pitch and volume dynamically scale as you bring your hands together.

### ♥ Shapes Mode — `#ff6bca`
Pose recognition that triggers visual geometry:
- **♥ Heart**: Bring both palms together with fingers spread open → animated parametric heart with radial gradient and pulsating shine.
- **✌ Peace**: Extend index and middle fingers with ring and pinky curled → glowing peace emblem.
- **💥 Star Burst**: Clench both hands into fists → rotating 8-point golden star with a 25-particle explosion.

### ✏ Write Mode — `#6bb5ff`
Turn your hand into a mid-air paintbrush:
- **Point**: Extend index finger to draw smooth Bézier curves with cycling hues.
- **Pinch (Pen Up)**: Pinch thumb and index together to lift the pen and finalize the stroke.
- **Shake to Clear**: Rapidly shake an open palm to fill the clearing ring and wipe the canvas, or click the bottom-right clear button.

---

## 🧪 Digital Playground (`digital_playground.html`)

Located in [`digital_playground.html`](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/digital_playground.html).

### 🖐️ 7 Hands-Free Webcam Gestures
| Gesture | Hand Pose | Simulation Action |
|:---|:---|:---|
| ☝️ **Point** | Index extended, others curled | **Paint**: Emits continuous streams of the active element at your fingertip |
| ✋ **Open Palm** | All fingers spread outward | **Repel Shield**: Creates an outward repulsive force field deflecting particles |
| ✊ **Fist** | All fingers curled inward | **Attract Gravity**: Creates an inward gravitational vortex pulling particles in |
| ✌️ **Peace Sign** | Index + middle up, others curled | **Nova Burst**: Detonates an explosive radial blast of 100+ high-velocity particles |
| 🤏 **Pinch** | Thumb & index touching | **Pause Clutch**: Temporarily clutches emission and pauses drawing |
| 🤘 **Rock-On** | Index & pinky extended | **Cycle Material**: Cycles to the next element (Water → Fire → Smoke → Sparks → Plasma → Gravity) |
| 👍 **Thumbs Up** | Thumb extended upward | **Turbo Jet**: Fires a high-density upward jet stream of energized particles |

### 🔬 Laboratory Controls
- **Brush Size**: 8 px to 90 px emitter radius.
- **Emission Rate**: 10% to 100% particle density.
- **Force Multiplier**: 0% to 100% velocity and force field influence.
- **Particle Lifetime**: 2.0 s to 14.0 s persistence.
- **Toggles**: Real-time toggles for Gravity, Fluid Turbulence, and Particle Trails.

---

## 🤌 Gestures Reference

### Desktop Virtual Mouse (`main.py`)
| Gesture | Hand Pose | OS Action |
|:---|:---|:---|
| ☝️ **Point** | Index extended | Moves system cursor |
| 🤏 **Left Click** | Thumb + index pinch | Single left click (anchor stabilized) |
| ✊ **Drag & Drop** | Thumb + index held (>0.4s) | Mouse down & drag |
| ✌️ **Double Click** | Thumb + middle pinch | Double click |
| 💍 **Right Click** | Thumb + ring pinch | Context menu right click |
| ✊ **Scroll** | Clenched fist moved vertically | Smooth scroll up / down |
| ✋ **Rest** | Open palm | Disables inputs (safe rest pose) |
| 👏 **Double Clap** | Two claps in rapid succession | Opens YouTube |

### Handy AI Core (`index.html`)
| Gesture | Mode | Recognition Criteria | Action |
|:---|:---|:---|:---|
| ⚡ **Pinch** | Play | Thumb tip to index tip < 40px | Electric zap + ripple ring + particle burst |
| ♥ **Heart** | Shapes | Both palms close (<240px), fingers spread | Animated glowing parametric heart |
| ✌ **Peace** | Shapes | Index + middle up, ring + pinky folded | Glowing neon peace symbol |
| 💥 **Star Burst** | Shapes | Both hands closed into fists | Rotating 8-point star + particle explosion |
| ✏ **Air Draw** | Write | Index finger extended | Continuous quadratic Bézier stroke |
| ✋ **Pen Up** | Write | Thumb + index pinch | End active stroke without drawing |
| 🌊 **Shake Clear** | Write | Rapid lateral palm velocity | Progressively wipes canvas clean |

### Digital Playground (`digital_playground.html`)
| Gesture | Hand Pose | Simulation Action |
|:---|:---|:---|
| ☝️ **Point** | Index extended | Paints active elemental material |
| ✋ **Open Palm** | 4–5 fingers extended wide | Repels particles with rotating force shield |
| ✊ **Fist** | All fingers clenched | Attracts particles into a gravitational center |
| ✌️ **Peace** | Index + middle extended | Fires Nova Particle Burst |
| 🤏 **Pinch** | Index + thumb touching | Clutch: pauses particle emission |
| 🤘 **Rock-On** | Index + pinky extended | Cycles through materials hands-free |
| 👍 **Thumbs Up** | Thumb extended upward | Turbo particle stream |

---

## 🛠️ Tech Stack

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                               Handy AI Suite                                │
├──────────────────────────────────────┬──────────────────────────────────────┤
│       Desktop Virtual Mouse          │          Web Creative Suite          │
│       (Python System Layer)          │         (Browser-Native Apps)        │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ • Python 3.10 – 3.12                 │ • Modern Vanilla JavaScript (ES6+)   │
│ • OpenCV (cv2) Video Pipeline        │ • HTML5 Canvas 2D Multi-layer Engine │
│ • Google MediaPipe Hands (Python)    │ • Google MediaPipe Hands (WASM/CDN)  │
│ • PyAutoGUI (Native OS Cursor & Keys)│ • Web Audio API (Real-time Synth)    │
│ • SoundDevice & NumPy (Acoustic FFT) │ • Verlet & Euler Physics Solvers     │
│ • Native Cross-Platform Threads      │ • Zero bundlers · Zero npm runtime   │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Canvas Layering Architecture (Web Apps)
```
Layer 5  ─  Interactive UI & Glassmorphism Panels (Top bar, sliders, toasts)
Layer 4  ─  Drawing & Skeleton Canvas (Bézier strokes, bone lines, AR tags)
Layer 3  ─  Particle & FX Canvas (Elemental particles, force ripples, stars)
Layer 2  ─  Atmospheric Background (Matrix Katakana rain / gradient mesh)
Layer 1  ─  Webcam Video Feed (<video> mirrored horizontally)
```

---

## 📁 Project Structure

```
Handy-AI/
├── hands-free virtual mouse/
│   ├── main.py              # 🖱️ Desktop virtual mouse, gesture solver & clap listener
│   ├── requirements.txt     # Python dependencies (mediapipe, pyautogui, sounddevice)
│   └── readme.md            # Standalone virtual mouse guide & tuning tips
├── index.html               # 🖐️ Handy AI Web Flagship (Play, Shapes, Write, Audio Synth)
├── digital_playground.html  # 🧪 Digital Playground Pro (6 Elements, 7 Gestures, AR Skeleton)
├── playground .html         # ⚡ Particle Lab Lite (Streamlined physics & quick hand tracking)
├── .gitignore               # Ignored environments, bytecode, and OS caches
└── README.md                # 📖 Comprehensive suite documentation & gesture manual
```

---

## 🔧 Troubleshooting

| Issue | Environment | Root Cause | Solution |
|:---|:---|:---|:---|
| **Mouse doesn't move or click** | macOS Desktop | Accessibility permission missing | Open **System Settings > Privacy & Security > Accessibility**, enable your terminal app (Terminal/iTerm/VS Code), and restart it. |
| **Microphone not detecting claps** | Desktop | Mic permission or high threshold | Check microphone privacy permissions; press `-` in preview to lower threshold, or verify with `python main.py --check`. |
| **Camera feed is black** | macOS Desktop | Camera permission missing | Allow your terminal in **System Settings > Privacy & Security > Camera**, then restart the terminal. |
| **`module 'mediapipe' has no attribute 'solutions'`** | Desktop | MediaPipe v0.10.15+ removed legacy API | Pin to supported release: `pip install "mediapipe==0.10.14"`. |
| **`pip install mediapipe` fails** | Desktop | Python 3.13+ incompatible wheels | Use Python 3.10, 3.11, or 3.12 (`python3.12 -m venv .venv`). |
| **Webcam blocked in browser** | Web Suite | Security origin restriction | Serve via `python3 -m http.server 8080` and access over `http://localhost:8080` (not bare `file://`). |
| **Cursor jitter** | Desktop / Web | Insufficient lighting or distance | Maintain 40–80 cm distance from camera in a well-lit area; coordinate smoothing is enabled by default. |

---

## 🌐 Browser & OS Compatibility

| Platform | Component | Support Status | Notes |
|:---|:---|:---|:---|
| **macOS** | Desktop Virtual Mouse | ✅ Supported | Requires Camera, Microphone, and Accessibility permissions |
| **Windows** | Desktop Virtual Mouse | ✅ Supported | Full PyAutoGUI native driver support |
| **Linux** | Desktop Virtual Mouse | ⚠️ Supported | Requires X11 display server for PyAutoGUI pointer control |
| **Google Chrome / Edge** | Web Suite | ✅ Recommended | Hardware-accelerated WebAssembly & Web Audio |
| **Firefox** | Web Suite | ⚠️ Functional | Canvas 2D supported; slightly higher CPU utilization |
| **Safari** | Web Suite | ⚠️ Functional | Requires explicit camera permissions; Web Audio activates upon first click |

---

## 🤝 Contributing

Contributions are welcomed! Potential areas for expansion:
- 💡 Additional gesture recognitions (OK sign, Spock vulcan salute, three-finger window switching)
- 🧪 New elemental materials (Electricity, Liquid Mercury, Black Hole)
- 🔊 Web Audio sound effects for the particle physics playground
- 📱 Mobile web touch-and-motion hybrid gestures

```bash
git checkout -b feature/new-awesome-feature
git commit -m "feat: add new gesture interaction"
git push origin feature/new-awesome-feature
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Credits

Built with:
- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html) by Google
- [OpenCV](https://opencv.org/) for computer vision and video stream transformations
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for cross-platform OS automation
- [SoundDevice](https://python-sounddevice.readthedocs.io/) & [NumPy](https://numpy.org/) for acoustic audio processing
- [Google Fonts](https://fonts.google.com/) — [Syne](https://fonts.google.com/specimen/Syne), [DM Mono](https://fonts.google.com/specimen/DM+Mono), and [Inter](https://fonts.google.com/specimen/Inter)

---

<p align="center">
  <sub>Made with 🖐️, ❤️, and code</sub>
</p>
