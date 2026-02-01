# 👁️ Open Vision Command Center v2.0 (SOTA Edition)

**Open Vision** is a professional-grade, real-time visual intelligence platform. Designed as a high-fidelity monitoring system, it bridges the gap between raw computer vision and actionable situational awareness.

## 🚀 Key Innovation: Parallel AI Orchestration
Unlike standard detection scripts, Open Vision runs on a **Decoupled Multi-Threaded Engine**. This ensures that the Camera Feed, AI Inference (YOLO11), and Human Analytics (DeepFace) run on separate hardware threads, delivering a smooth 30+ FPS experience even with heavyweight models.

## 🧠 Core Intelligence Modules
- **Object Perception (YOLO11-HighFidelity):** Real-time detection of 80+ object classes with advanced attribute extraction (Color recognition & Scale analysis).
- **Human Analytics (DeepFace Logic):** Instant demographic profiling including **Age Estimation**, **Gender Identification**, and **Emotional State (Mood)** analysis.
- **Neural Interaction (Asynchronous TTS):** A built-in voice personality that provides hands-free intelligence reports and critical alerts.
- **Tactical HUD:** A premium, data-rich Command Center GUI designed for professional surveillance environments.

## 🛠️ Technical Architecture
- **Vision Engine:** Ultralytics YOLO11 (Extra-Large/Medium Support)
- **Intelligence Layer:** DeepFace Meta-Analysis
- **Concurrency:** Python threading & Queue-based frame buffer
- **UI Framework:** Optimized OpenCV HUD with Tactical Overlays
- **Logging:** Structured JSON temporal data logs

## 📥 Installation & Usage
1. **Clone & Setup:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Execute Command Center:**
   ```bash
   python main.py
   ```

---
*Developed for elite situational awareness and real-time visual forensics.*
