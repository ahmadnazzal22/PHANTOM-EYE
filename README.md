# 👁 PHANTOM EYE
### Intelligent Surveillance System

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![YOLO](https://img.shields.io/badge/YOLOv8-Ultralytics-purple?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Web_UI-black?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🎯 What is PHANTOM EYE?

PHANTOM EYE is a real-time AI-powered surveillance system that detects and tracks
people, vehicles, and animals through live camera or video files.
Every detected object is classified, labeled, and color-coded instantly.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🔍 Motion Detection | Detects every moving object in real-time |
| 👤 Face Recognition | Identifies known persons from your database |
| 🚗 License Plate Reader | Reads and logs vehicle plate numbers via OCR |
| 🐾 Animal Detection | Identifies animals by species |
| 🔴 NEW / 🔵 KNOWN | Color-coded bounding boxes for new vs known objects |
| 💾 Auto Save | Saves unknown faces and plate images automatically |
| 🌐 Web Interface | Professional dark UI accessible from any browser |
| ⚡ Optimized Speed | Frame skipping + caching for real-time performance |

---

## 🖥 Demo



🔴 Red Box  → New / Unknown object (first time seen)
🔵 Blue Box → Known object (already in database)


---

```html
<div class="project-structure">
    <h2>📁 Project Structure</h2>

    <pre>
👁 phantom-eye/
│
├── README.md
├── app.py
├── tracker.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── known_faces/
│   ├── ahmad.jpg
│   └── sara.jpg
│
├── detected_faces/
│   └── face_20240101_120000.jpg
│
└── detected_plates/
    └── plate_ABC123_20240101.jpg
    </pre>
</div>
```

```css
.project-structure {
    background: #111;
    color: #00ff88;
    padding: 20px;
    border-radius: 12px;
    font-family: Consolas, monospace;
    margin-top: 20px;
}

.project-structure h2 {
    color: white;
    margin-bottom: 15px;
}

.project-structure pre {
    white-space: pre-wrap;
    margin: 0;
}
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/ahmadnazzal22/phantom-eye.git
cd phantom-eye


2. Install dependencies

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install ultralytics easyocr insightface onnxruntime opencv-python flask


3. Add known faces (optional)

Place .jpg or .png photos in the known_faces/ folder.
Name each file with the person's name:
  known_faces/ahmad.jpg
  known_faces/sara.jpg


4. Run

# Windows
$env:PYTHONIOENCODING = "utf-8"
python app.py


Then open your browser at:

http://localhost:5000


🚀 Usage

|Button        |Action                      |
|--------------|----------------------------|
|📷 LIVE CAMERA |Start webcam feed           |
|📁 VIDEO FILE  |Load a local video file     |
|⛔ STOP        |Stop the stream             |
|🔄 RELOAD FACES|Refresh known faces database|

🧠 How It Works

Video Frame
    ↓
YOLOv8 — Detect objects (person / car / animal)
    ↓
┌─────────────────────────────┐
│  Person → InsightFace       │ → Known? Blue | Unknown? Red + Save
│  Car    → EasyOCR           │ → Read plate + Save image
│  Animal → YOLO label        │ → Show species
└─────────────────────────────┘
    ↓
Draw bounding boxes + labels
    ↓
Stream to Web UI via Flask


⚡ Performance Optimizations

	•	Frame skipping — Processes every 2nd frame
	•	Resolution scaling — Resizes to 640px before YOLO
	•	Face cache — Avoids re-analyzing same region
	•	OCR throttle — Reads plates every 10 frames only
	•	InsightFace 160px — Small crops for faster recognition

🛠️ Tech Stack

	•	YOLOv8 — Object detection
	•	InsightFace — Face recognition
	•	EasyOCR — License plate reading
	•	OpenCV — Video processing
	•	Flask — Web server & streaming
	•	Orbitron Font — UI typography

📋 Requirements

Python 3.10+
torch
ultralytics
easyocr
insightface
onnxruntime
opencv-python
flask
numpy


👤 Author

Ahmad Nazzal

	•	GitHub: @ahmadnazzal22
	•	Built with ❤️ using Python & AI

📜 License

MIT License — Free to use and modify.

“See everything. Miss nothing.”
— PHANTOM EYE 👁
