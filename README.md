# 👁 PHANTOM EYE

### Intelligent AI-Powered Surveillance System

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![YOLO](https://img.shields.io/badge/YOLOv8-Ultralytics-purple?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Web_UI-black?style=for-the-badge\&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🎯 What is PHANTOM EYE?

**PHANTOM EYE** is a real-time AI-powered surveillance platform designed to detect, classify, track, and identify objects from live cameras or video files.

The system combines modern computer vision technologies to recognize:

* 👤 People
* 🚗 Vehicles
* 🔢 License Plates
* 🐾 Animals

Each detected object is analyzed, labeled, tracked, and displayed in real time through a modern web dashboard.

---

## ✨ Features

| Feature                      | Description                                    |
| ---------------------------- | ---------------------------------------------- |
| 🔍 Motion Detection          | Detects moving objects in real-time            |
| 👤 Face Recognition          | Identifies known persons from a local database |
| 🚗 License Plate Recognition | Reads and logs vehicle plates using OCR        |
| 🐾 Animal Detection          | Detects and classifies animal species          |
| 🔴 New Object Detection      | Highlights first-time detections               |
| 🔵 Known Object Tracking     | Marks previously recognized identities         |
| 💾 Auto Save                 | Saves unknown faces and detected plates        |
| 🌐 Web Dashboard             | Access from any browser                        |
| ⚡ Real-Time Performance      | Optimized for speed and low latency            |
| 📹 Live Camera Support       | Monitor webcams and IP cameras                 |
| 📁 Video File Processing     | Analyze recorded videos                        |

---

## 🖥 Demo

### Detection Colors

🔴 **Red Box**
→ New / Unknown Object

🔵 **Blue Box**
→ Known / Previously Identified Object

---

## 📁 Project Structure

```text
👁 phantom-eye/
│
├── README.md                 # Project documentation
├── app.py                    # Flask web application
├── tracker.py                # Detection & tracking engine
│
├── templates/
│   └── index.html            # Web interface
│
├── static/
│   └── style.css             # UI styling
│
├── known_faces/              # Registered persons database
│   ├── ahmad.jpg
│   └── sara.jpg
│
├── detected_faces/           # Saved unknown faces
│   └── face_20240101_120000.jpg
│
└── detected_plates/          # Saved license plate captures
    └── plate_ABC123_20240101.jpg
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ahmadnazzal22/phantom-eye.git
cd phantom-eye
```

### 2️⃣ Install Dependencies

#### PyTorch (CPU Version)

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

#### Main Requirements

```bash
pip install ultralytics
pip install easyocr
pip install insightface
pip install onnxruntime
pip install opencv-python
pip install flask
pip install numpy
```

Or:

```bash
pip install -r requirements.txt
```

---

## 👤 Add Known Faces (Optional)

Place images inside:

```text
known_faces/
```

Example:

```text
known_faces/ahmad.jpg
known_faces/sara.jpg
```

The filename will be used as the person's identity.

---

## 🚀 Running the Application

### Windows

```powershell
$env:PYTHONIOENCODING="utf-8"
python app.py
```

### Linux / macOS

```bash
python app.py
```

---

## 🌐 Open Dashboard

After starting the server:

```text
http://localhost:5000
```

Open the URL in your browser.

---

## 🎮 Usage

| Button          | Action                       |
| --------------- | ---------------------------- |
| 📷 LIVE CAMERA  | Start webcam stream          |
| 📁 VIDEO FILE   | Load a local video           |
| ⛔ STOP          | Stop current stream          |
| 🔄 RELOAD FACES | Refresh known faces database |

---

## 🧠 System Workflow

```text
Video Frame
    │
    ▼
YOLOv8 Detection
(Person / Vehicle / Animal)
    │
    ▼
┌─────────────────────────────────────┐
│ Person → InsightFace                │
│      └─ Known?  → Blue Box          │
│      └─ Unknown → Red Box + Save    │
│                                     │
│ Vehicle → EasyOCR                   │
│      └─ Read License Plate          │
│      └─ Save Plate Image            │
│                                     │
│ Animal → YOLO Species Label         │
└─────────────────────────────────────┘
    │
    ▼
Draw Bounding Boxes
    │
    ▼
Flask Live Stream
    │
    ▼
Web Dashboard
```

---

## ⚡ Performance Optimizations

* Frame Skipping (process every 2nd frame)
* Resolution Scaling (640px input)
* Face Recognition Cache
* OCR Throttling
* Lightweight Face Crops
* Efficient Object Tracking

---

## 🛠 Technology Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| YOLOv8       | Object Detection          |
| InsightFace  | Face Recognition          |
| EasyOCR      | License Plate Recognition |
| OpenCV       | Video Processing          |
| Flask        | Web Server                |
| NumPy        | Numerical Operations      |
| ONNX Runtime | Model Inference           |

---

## 📋 Requirements

```text
Python 3.10+
torch
ultralytics
easyocr
insightface
onnxruntime
opencv-python
flask
numpy
```

---

## 🔮 Future Enhancements

* Multi-Camera Support
* IP Camera Integration
* Telegram Alerts
* Email Notifications
* Database Logging
* Person Re-Identification
* Vehicle Tracking
* Heatmaps & Analytics
* Dark Mode Dashboard Enhancements

---

## 👨‍💻 Author

**Ahmad Nazzal**

GitHub: @ahmadnazzal22

Built with ❤️ using Python, Computer Vision, and Artificial Intelligence.

---

## 📜 License

MIT License

Free to use, modify, and distribute.

---

## ⭐ Support

If you like this project:

⭐ Star the repository

🍴 Fork the project

🛠 Contribute improvements

---

> **"See Everything. Miss Nothing."**
>
> **— PHANTOM EYE 👁**
