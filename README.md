<p align="center">
  <img src="https://img.shields.io/badge/Vanilla-HTML%2FCSS%2FJS-f7df1e?style=for-the-badge" alt="Vanilla JS"/>
  <img src="https://img.shields.io/badge/MediaPipe-Hands-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="MediaPipe"/>
  <img src="https://img.shields.io/badge/Web%20Audio-API-ff6bca?style=for-the-badge" alt="Web Audio"/>
  <img src="https://img.shields.io/badge/Zero-Dependencies-7cffc4?style=for-the-badge" alt="Zero Dependencies"/>
</p>

<h1 align="center">
  🖐️ Handy AI
</h1>

<p align="center">
  <strong>Gesture Intelligence Platform</strong><br/>
  <sub>Real-time hand tracking · Gesture physics · Air drawing — all in a single HTML file</sub>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-modes">Modes</a> •
  <a href="#-gestures">Gestures</a> •
  <a href="#%EF%B8%8F-tech-stack">Tech Stack</a> •
  <a href="#-credits">Credits</a>
</p>

---

## ✨ Overview

**Handy AI** is a fullscreen, browser-based hand gesture experience powered by [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html). It transforms your webcam feed into an interactive playground where you can draw in mid-air, form shapes with both hands, and trigger particle effects — all running at real-time framerates with zero server-side processing.

Everything lives in a **single `index.html` file** — no build tools, no frameworks, no npm installs.

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/handy-ai.git
cd handy-ai

# Open directly in your browser
open index.html          # macOS
start index.html         # Windows
xdg-open index.html      # Linux
```

> [!NOTE]
> **Camera access is required.** Best experienced in **Chrome** or **Edge** on desktop.
> The app loads MediaPipe models from CDN on first launch (~5 MB).

Or serve it locally for full functionality:

```bash
python3 -m http.server 8080
# Then visit http://localhost:8080
```

---

## 🎯 Features

| Category | Details |
|:---|:---|
| 🖐️ **Hand Tracking** | Up to 2 hands, 21 landmarks each, via MediaPipe Hands |
| 🎨 **Three Modes** | Play, Shapes, and Write — each with unique interactions |
| ✨ **Particle System** | Gravity-affected particles with fade, sparkle trails from fingertips |
| 🌊 **Ripple Effects** | Expanding double-ring ripples on pinch events |
| ⚡ **Lightning Bolts** | Jagged procedural lightning between close fingertips |
| 🔮 **Wireframe Mandala** | Rotating geometric pattern connecting all 10 fingertips |
| ✏️ **Air Drawing** | Smooth Bézier strokes with hue-cycling colors and glow |
| 🔊 **Spatial Audio** | Web Audio API — zap, pop, and continuous proximity hum |
| 🌧️ **Matrix Rain** | Katakana character rain that reacts to hand velocity |
| 📊 **Live HUD** | FPS counter, hand count, gesture labels, toast notifications |
| 🎭 **Film Grain** | SVG fractalNoise overlay for cinematic texture |
| 📱 **Responsive** | Adapts to mobile screens with icon-only mode buttons |

---

## 🎮 Modes

### ▶ Play Mode — `#7cffc4`

The default exploration mode. Your hands become glowing, color-shifting skeletons with sparkle particle trails streaming from every fingertip.

- **Pinch** thumb + index to trigger ⚡ electric zap with ripple + particle burst
- **Two hands** — gradient lines connect matching fingertips across both hands
- **Close tips** (<140px) — jagged lightning bolts arc between fingers
- **Mandala** — a rotating wireframe pattern connects all 10 fingertips at their centroid
- **Proximity hum** — a continuous oscillator whose pitch scales with inter-hand distance

### ♥ Shapes Mode — `#ff6bca`

Form recognizable shapes using specific hand poses. Requires at least one hand (two hands for Heart and Star Burst).

- **♥ Heart** — Both palms close together, fingers spread open → animated parametric heart with radial gradient, pulsing glow, and inner highlight shine
- **✌ Peace** — Index + middle fingers extended, ring + pinky curled → glowing peace symbol
- **💥 Star Burst** — Both hands clenched into fists → rotating 8-point star with gold gradient + 25-particle explosion

### ✏ Write Mode — `#6bb5ff`

Turn your index finger into a pen and draw in mid-air.

- **Point** index finger to draw — smooth quadratic Bézier strokes with hue cycling
- **Pinch** to lift the pen and save the stroke
- **Shake** open palm to clear canvas (progress ring fills as shake builds)
- **Clear button** also available in bottom-right corner

---

## 🤌 Gestures

| Gesture | Mode | How To | Effect |
|:---|:---|:---|:---|
| ⚡ Pinch | Play | Touch thumb + index tips | Ripple + particles + zap sound |
| ♥ Heart | Shapes | Both palms close, fingers spread | Animated parametric heart |
| ✌ Peace | Shapes | Index + middle up, others curled | Glowing peace symbol |
| 💥 Star Burst | Shapes | Both hands fisted | Rotating star + particle explosion |
| ✏ Draw | Write | Point index finger | Smooth air-drawing stroke |
| ✋ Pen Up | Write | Pinch thumb + index | Save current stroke |
| 🌊 Clear | Write | Shake open palm rapidly | Clear all drawings |

---

## 🛠️ Tech Stack

```
┌─────────────────────────────────────────────┐
│  Single index.html file                     │
│                                             │
│  ├── HTML5          Structure & semantics   │
│  ├── CSS3           Design system & anims   │
│  ├── Vanilla JS     All logic & rendering   │
│  ├── Canvas 2D      Multi-layer rendering   │
│  ├── MediaPipe      Hand landmark detection │
│  ├── Web Audio API  Sound synthesis         │
│  └── Google Fonts   Syne 800 + DM Mono     │
│                                             │
│  CDN Dependencies:                          │
│  ├── @mediapipe/hands@0.4                   │
│  └── @mediapipe/camera_utils@0.3            │
└─────────────────────────────────────────────┘
```

### Design Tokens

| Token | Value | Usage |
|:---|:---|:---|
| `--bg` | `#03020a` | Background color |
| `--accent` | `#7cffc4` | Play mode / primary green |
| `--accent2` | `#ff6bca` | Shapes mode / pink |
| `--accent3` | `#6bb5ff` | Write mode / blue |
| Font (headings) | Syne 800 | Logo, toasts, panel headers |
| Font (UI) | DM Mono 400/500 | All monospace interface text |

### Canvas Layers (z-index order)

```
Layer 5  ─  UI (top bar, HUD, toasts, help panel)
Layer 4  ─  drawCanvas (air-drawing strokes)
Layer 3  ─  fxCanvas (skeleton, particles, ripples, shapes)
Layer 2  ─  bgCanvas (matrix rain)
Layer 1  ─  <video> (mirrored webcam feed)
```

---

## ⚙️ MediaPipe Configuration

| Parameter | Value |
|:---|:---|
| `maxNumHands` | 2 |
| `modelComplexity` | 1 |
| `minDetectionConfidence` | 0.72 |
| `minTrackingConfidence` | 0.72 |
| Camera resolution | 1920×1080 (ideal) |
| Frame rate | 30 fps (ideal) |

---

## 🔊 Audio System

All sounds are synthesized in real-time using the **Web Audio API** — no audio files needed.

| Sound | Oscillator | Behavior |
|:---|:---|:---|
| **Zap** | Sawtooth | 700 Hz → 30 Hz exponential ramp (120ms) |
| **Pop** | Sine | freq → freq×0.5 ramp (80ms) |
| **Hum** | Sine (continuous) | 80–360 Hz, gain scales with two-hand proximity |

---

## 📁 Project Structure

```
handy-ai/
└── index.html    ← Everything lives here (HTML + CSS + JS)
```

Yes, that's it. One file. ~1,200 lines. Zero dependencies to install.

---

## 🌐 Browser Support

| Browser | Support |
|:---|:---|
| Chrome 90+ | ✅ Recommended |
| Edge 90+ | ✅ Recommended |
| Firefox 90+ | ⚠️ Works, may have lower FPS |
| Safari 15+ | ⚠️ Limited WebRTC support |
| Mobile Chrome | ✅ Responsive layout |
| Mobile Safari | ⚠️ Camera API limitations |

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas:

- 🎯 Add new gesture recognitions (thumbs up, OK sign, rock on)
- 🎨 New visual effects (trails, kaleidoscope, mirror mode)
- 🔊 Richer audio (chords, ambient soundscapes)
- 📱 Improved mobile performance
- 🧪 Gesture recording & playback

```bash
# Fork → Branch → Code → PR
git checkout -b feature/my-awesome-gesture
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Credits

Built with:
- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html) by Google
- [Syne](https://fonts.google.com/specimen/Syne) & [DM Mono](https://fonts.google.com/specimen/DM+Mono) from Google Fonts
- Web Audio API for sound synthesis

---

<p align="center">
  <sub>Made with 🖐️ and ❤️</sub>
</p>
