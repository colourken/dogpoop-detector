# 💩 DogPoopAI — Dog Poop Detection for Autonomous Robots

**By Samlyn Robotics Ltd.**  
© 2026 Samlyn Robotics Ltd. All rights reserved.

---

## 🌐 Live Demo

**https://colourken.github.io/dogpoop-detector/**

Open on any mobile browser. No installation required.

---

## 📱 What This Is

A real-time dog poop detector running entirely in your browser.  
Built for testing whether AI detection is **stable enough for robot control**.

> "Detected" is not enough. "Stably detected" is what matters.

---

## 🤖 Features

### Detection
- YOLOv8n model trained on outdoor European park scenes
- ONNX Runtime Web — model runs locally on your device, no server
- WebGPU backend (fast) with automatic WASM fallback

### Stability Layer (Robot Perception)
- **Box smoothing** — moving average over last 5 detections
- **Confidence EMA** — `smoothed = 0.7 × prev + 0.3 × raw`
- **Hysteresis** — appears at 0.55, disappears below 0.40
- **Decision layer** — 5 consecutive frames before `target_locked`
- **Target memory** — holds target for up to 10 missing frames

### Robot State Machine
```
SEARCHING → TARGET_LOCKED → APPROACHING → ALIGNING → LOST_TARGET
```

### Approach Guidance
- Real-time direction guidance: **Left / Right / Center**
- Offset percentage from screen centre
- Visual guidance line from centre to target

### Debug Panel
- Raw confidence / Smoothed confidence
- target_locked status
- Detected / Missing frame count
- Centre offset X/Y
- Target area %
- FPS / Backend (WebGPU or WASM)

### Detection History Graph
- 30-frame smoothed confidence graph
- Threshold lines at 0.40 (red) and 0.55 (blue)

---

## 🧠 Model Versions

| Version | mAP50 | Dataset | Notes |
|---------|-------|---------|-------|
| v6 | 0.666 | 368 images | Base model |
| v7 | 0.688 | 911 images | +Summer batches +Hard Negatives |

Switch between v6 and v7 in the model selector to compare performance.

---

## 🔬 Purpose

This is a **robot perception testing platform**, not a consumer app.

Primary goal: Validate whether the AI signal is stable enough to drive physical robot actions.

Built as part of Samlyn Robotics' outdoor autonomous dog waste collection robot project.

---

## ⚠️ Legal

© 2026 Samlyn Robotics Ltd. All rights reserved.  
Unauthorized copying, redistribution, or commercial use of this software or trained models is prohibited.

---

## 📬 Contact

**Samlyn Robotics Ltd.**  
samlynrobotics@gmail.com  
https://poopbot.netlify.app
