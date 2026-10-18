<p align="center">
  <img src="https://img.shields.io/badge/Vanilla-HTML%2FCSS%2FJS-f7df1e?style=for-the-badge" alt="Vanilla JS"/>
  <img src="https://img.shields.io/badge/MediaPipe-Hands-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe"/>
  <img src="https://img.shields.io/badge/Web%20Audio-API-ff6bca?style=for-the-badge" alt="Web Audio"/>
  <img src="https://img.shields.io/badge/Physics%20Engine-Particle%20Sim-7bd8ff?style=for-the-badge" alt="Physics Engine"/>
  <img src="https://img.shields.io/badge/Zero-Dependencies-7cffc4?style=for-the-badge" alt="Zero Dependencies"/>
</p>

<h1 align="center">
  🖐️ Handy AI
</h1>

<p align="center">
  <strong>Gesture Intelligence & Interactive Physics Suite</strong><br/>
  <sub>Real-time hand tracking · Fluid particle dynamics · Gesture-controlled physics · Air drawing — zero dependencies</sub>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-the-suite">The Suite</a> •
  <a href="#-features">Features</a> •
  <a href="#-handy-ai-flagship">Handy AI Core</a> •
  <a href="#-digital-playground">Digital Playground</a> •
  <a href="#-gestures-reference">Gestures</a> •
  <a href="#%EF%B8%8F-tech-stack">Tech Stack</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-credits">Credits</a>
</p>

---

## ✨ Overview

**Handy AI** is a browser-native computer vision and creative computing suite powered by [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html). It transforms standard webcam video feeds into interactive gesture-driven experiences — from drawing glowing art in mid-air and conjuring spatial audio to manipulating real-time fluid particle physics simulations with hand poses.

The repository includes **three standalone web applications**, each self-contained with zero build tools, zero frameworks, and zero npm dependencies:

1. **[index.html](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/index.html)** — **Handy AI Core**: The flagship gesture intelligence platform featuring Play, Shapes, and Write modes, procedural Web Audio synthesis, and multi-layer canvas rendering.
2. **[digital_playground.html](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/digital_playground.html)** — **Digital Playground (Pro)**: A full-featured interactive particle physics laboratory with 6 elemental materials, 7 webcam hand gestures, live augmented reality skeleton overlays, and comprehensive force controls.
3. **[playground .html](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/playground%20.html)** — **Particle Lab (Lite)**: A streamlined, ultra-fast particle sandbox with quick index-finger tracking, pinch pause clutch, and fluid-like visual dynamics.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/oseyosmanyildiz/handy-ai.git
cd handy-ai

# Open any of the experiences directly in your browser:

# 1. Handy AI Core (Flagship gesture platform)
open index.html          # macOS
start index.html         # Windows
xdg-open index.html      # Linux

# 2. Digital Playground (Full gesture & particle physics lab)
open digital_playground.html

# 3. Particle Lab Lite (Streamlined physics sandbox)
open "playground .html"
```

> [!NOTE]
> **Webcam access is required for hand tracking.**
> For security reasons, modern browsers require camera permissions to be granted over `localhost` or `HTTPS`. To serve the entire suite locally:
> ```bash
> python3 -m http.server 8080
> ```
> Then visit `http://localhost:8080` in **Chrome** or **Edge** on desktop. MediaPipe models load on-demand from CDN on first launch (~5 MB).

---

## 📦 The Suite

| Application | File | Core Focus | Interaction Methods | Key Features |
|:---|:---|:---|:---|:---|
| **Handy AI Core** | [`index.html`](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/index.html) | Gesture intelligence, air drawing & audio | Dual-hand tracking, pinch gestures, palm gestures | 3 Modes (Play, Shapes, Write), Web Audio synthesizer, Bézier air drawing, matrix rain |
| **Digital Playground** | [`digital_playground.html`](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/digital_playground.html) | Fluid-like particle physics & elemental simulation | 7 AI webcam gestures, mouse drag, touch | 6 Materials, AR skeleton overlay with live wrist tags, floating gesture badge, force fields |
| **Particle Lab** | [`playground .html`](file:///Users/oseyosmanyildiz/Desktop/Handwave%20Tracker/playground%20.html) | Lightweight interactive particle dynamics | Index finger pointing, pinch clutch, pointer | Fast-launching sandbox, 6 materials, turbulence & gravity toggles, force controls |

---

## 🎯 Features

### 🖐️ Computer Vision & Tracking
- **MediaPipe Hands Integration**: Real-time 21-landmark 3D coordinate detection running client-side at up to 60 FPS.
- **Single & Dual Hand Detection**: Supports two-handed interactions, inter-hand proximity hum, and multi-hand shape formation.
- **AR Skeleton & HUD Overlays**: Luminous dual-layer bones, energy crowns, live gesture name tags anchored to the wrist, and neon gesture status badges.
- **Gesture Hysteresis & Filtering**: Multi-frame temporal stability filtering to eliminate flickering gesture states, with exponential moving average (EMA) smoothing on coordinates.

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

## 🎮 Handy AI Flagship (`index.html`)

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

An advanced elemental particle laboratory fully operable hands-free via webcam gestures:

### 🖐️ 7 Hands-Free Webcam Gestures
| Gesture | Pose | Action & Effect |
|:---|:---|:---|
| ☝️ **Point** | Index extended, others curled | **Paint**: Emits continuous streams of the selected element at your fingertip |
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
┌─────────────────────────────────────────────────────────────┐
│                       Handy AI Suite                        │
│                                                             │
│  ├── Core              HTML5, Modern CSS3, Vanilla JS (ES6+)│
│  ├── Vision & AI       Google MediaPipe Hands & Camera Utils│
│  ├── Rendering         Canvas 2D Multi-layer Architecture   │
│  ├── Audio Engine      Web Audio API (Procedural Synthesis) │
│  ├── Physics Engine    Real-time Verlet & Euler Particle Sim│
│  └── Typography        Syne 800, DM Mono, Inter             │
│                                                             │
│  Zero build steps · Zero bundlers · Zero runtime npm deps   │
└─────────────────────────────────────────────────────────────┘
```

### Canvas Layering Architecture
```
Layer 5  ─  Interactive UI & Glassmorphism Panels (Top bar, sliders, toasts)
Layer 4  ─  Drawing & Skeleton Canvas (Bézier strokes, bone lines, AR tags)
Layer 3  ─  Particle & FX Canvas (Elemental particles, force ripples, stars)
Layer 2  ─  Atmospheric Background (Matrix Katakana rain / gradient mesh)
Layer 1  ─  Webcam Video Feed (<video> mirrored horizontally)
```

---

## ⚙️ MediaPipe Configuration

| Setting | Value | Description |
|:---|:---|:---|
| `maxNumHands` | 1–2 | Single-hand in physics labs; dual-hand in Handy AI flagship |
| `modelComplexity` | 0–1 | Optimized for real-time client performance |
| `minDetectionConfidence` | 0.55 – 0.72 | Fast hand acquisition |
| `minTrackingConfidence` | 0.50 – 0.72 | Rock-solid landmark tracking |
| Camera Target Resolution | 640×480 – 1920×1080 | Adaptive resolution scaling |

---

## 🔊 Audio Engine (`index.html`)

All sound effects are synthesized algorithmically in real-time using the **Web Audio API**:

| Sound | Oscillator | Frequency Ramp | Description |
|:---|:---|:---|:---|
| **Zap** | Sawtooth | 700 Hz → 30 Hz (120ms exponential) | Pinch trigger discharge |
| **Pop** | Sine | freq → freq × 0.5 (80ms ramp) | Mode switch & button activations |
| **Hum** | Sine (continuous) | 80 Hz – 360 Hz (proximity-controlled) | Proximity hum scaling with two-hand distance |

---

## 📁 Project Structure

```
handy-ai/
├── index.html               # 🖐️ Handy AI Flagship (Play, Shapes, Write, Audio Synth)
├── digital_playground.html  # 🧪 Digital Playground Pro (6 Elements, 7 Gestures, AR Skeleton)
├── playground .html         # ⚡ Particle Lab Lite (Streamlined physics & quick hand tracking)
└── README.md                # 📖 Comprehensive suite documentation & gesture guide
```

Every HTML file in this repository is **100% standalone and portable** — double-click to open or serve from any static web server.

---

## 🌐 Browser Support

| Browser | Desktop Support | Mobile Support | Notes |
|:---|:---|:---|:---|
| **Google Chrome** | ✅ Recommended (90+) | ✅ Full Support | Optimal WebGL & MediaPipe WebAssembly performance |
| **Microsoft Edge** | ✅ Recommended (90+) | ✅ Full Support | Chromium-backed, excellent framerates |
| **Mozilla Firefox** | ⚠️ Supported (90+) | ⚠️ Lower FPS | Canvas 2D and camera work; slightly higher CPU load |
| **Apple Safari** | ⚠️ Supported (15+) | ⚠️ Limited | Requires explicit camera permission; audio unlocks on tap |

---

## 🤝 Contributing

Contributions are welcomed! Potential areas for expansion:
- 💡 Additional gesture recognitions (OK sign, Spock vulcan salute, finger counting)
- 🧪 New elemental materials (Electricity, Liquid Mercury, Black Hole)
- 🔊 Web Audio sound effects for the particle physics playground
- 📱 Touch-optimized mobile gesture alternatives

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
- [Google Fonts](https://fonts.google.com/) — [Syne](https://fonts.google.com/specimen/Syne), [DM Mono](https://fonts.google.com/specimen/DM+Mono), and [Inter](https://fonts.google.com/specimen/Inter)
- Web Audio API & Canvas 2D

---

<p align="center">
  <sub>Made with 🖐️, ❤️, and code</sub>
</p>

