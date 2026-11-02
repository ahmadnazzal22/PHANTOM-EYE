# 👁 PHANTOM EYE
### AI-Powered Object Detection & Surveillance Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-purple?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-Web%20Dashboard-black?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🎯 Overview

**PHANTOM EYE** is a computer vision project designed to analyze live camera streams and recorded videos using AI-powered object detection, tracking, and recognition technologies.

The system combines YOLOv8, OpenCV, InsightFace, and EasyOCR to process video frames and display detected objects through a Flask-based web dashboard.

Depending on the enabled modules, it can analyze:

- 👤 People
- 🚗 Vehicles
- 🔢 License plates
- 🐾 Animals

The dashboard displays detection results, labels, and visual tracking indicators in an interactive interface.

## ✨ Features

| Feature | Description |
|---|---|
| Object Detection | Detects supported objects in video frames |
| Motion Analysis | Helps identify moving objects |
| Face Recognition | Compares detected faces with locally registered face data |
| License Plate OCR | Extracts text from supported vehicle plate images |
| Object Tracking | Tracks detected objects across processed frames |
| Detection Indicators | Uses different colors to distinguish detection states |
| Local Data Storage | Stores configured detection images and results |
| Web Dashboard | Displays the system through a browser interface |
| Live Camera Input | Supports compatible webcams and configured camera streams |
| Video Processing | Processes recorded video files |

> Feature availability and accuracy depend on the models, configuration, camera quality, and actual implementation.

## 🖥️ Detection Indicators

- 🔴 **Red Box:** New or unrecognized detection.
- 🔵 **Blue Box:** Previously recognized or tracked detection.

These colors represent the project's configured visual indicators; they do not guarantee the identity of a person or object.

## 🧠 System Workflow

```text
Camera Stream / Video File
          |
          v
     Video Frames
          |
          v
     YOLOv8 Detection
          |
          v
   Object Classification
          |
    +-----+----------+
    |                |
    v                v
  Person           Vehicle
    |                |
    v                v
InsightFace        EasyOCR
    |                |
    v                v
Face Matching    Plate Text
    |                |
    +-------+--------+
            |
            v
    Detection Results
            |
            v
    OpenCV Visualization
            |
            v
      Flask Live Stream
            |
            v
       Web Dashboard
```

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Main programming language |
| YOLOv8 / Ultralytics | Object detection |
| InsightFace | Face analysis and recognition |
| EasyOCR | Text recognition |
| OpenCV | Image and video processing |
| Flask | Web application and dashboard |
| PyTorch | Deep learning framework |
| ONNX Runtime | Model inference support |
| NumPy | Numerical operations |

## 📁 Project Structure

```text
phantom-eye/
│
├── app.py
├── tracker.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── known_faces/
├── detected_faces/
└── detected_plates/
```

*This is a simplified representation based on the supplied project structure. Update it to match the actual repository files.*

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ahmadnazzal22/phantom-eye.git
cd phantom-eye
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

If the project includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages according to the project's actual configuration:

```bash
pip install ultralytics easyocr insightface onnxruntime opencv-python flask numpy
```

Install the appropriate PyTorch build for your operating system and hardware using the official PyTorch installation instructions.

## 👤 Register Known Faces

If face recognition is enabled, place authorized reference images inside:

```text
known_faces/
```

Example:

```text
known_faces/
├── person_01.jpg
└── person_02.jpg
```

The filename can be used as a label by the application, depending on how the recognition module is implemented.

Only use images when you have the appropriate permission and a legitimate reason to process them.

## 🚀 Run the Application

**Windows PowerShell:**

```powershell
$env:PYTHONIOENCODING="utf-8"
python app.py
```

**macOS / Linux:**

```bash
python app.py
```

## 🌐 Open the Dashboard

After starting the Flask application, open:

```text
http://127.0.0.1:5000
```

The actual address and port depend on the Flask configuration in `app.py`.

## 🎮 Dashboard Controls

| Control | Action |
|---|---|
| LIVE CAMERA | Start a configured camera stream |
| VIDEO FILE | Select a recorded video |
| STOP | Stop the current processing session |
| RELOAD FACES | Reload the configured face data |

*Confirm that these controls and labels match the current dashboard before publishing.*

## ⚡ Performance Considerations

The supplied design describes several performance techniques:

- Frame skipping
- Input resolution scaling
- Face recognition caching
- OCR throttling
- Lightweight face crops
- Object tracking optimization

Actual performance depends on the hardware, input resolution, model configuration, and number of enabled processing modules.

## 🔐 Privacy & Responsible Use

PHANTOM EYE includes features that may process identifiable information, including faces and vehicle license plates.

- Use the system only in environments where monitoring is authorized.
- Obtain required permissions and follow applicable privacy laws.
- Protect stored face images, plate captures, and detection logs.
- Restrict access to the dashboard and stored data.
- Define appropriate retention and deletion policies.
- Do not treat automated recognition results as definitive proof of identity.

## 🔮 Future Enhancements

- Multi-camera management
- Improved IP camera integration
- Telegram and email notifications
- Database-backed event logging
- Person re-identification
- Vehicle tracking improvements
- Detection heatmaps and analytics
- Enhanced dashboard customization

## 👨‍💻 Author

**Ahmad Nazzal**

GitHub: [@ahmadnazzal22](https://github.com/ahmadnazzal22)

Built with Python, Computer Vision, and Artificial Intelligence.

## 📜 License

This project is presented as MIT licensed. Confirm that the repository contains a matching `LICENSE` file before publishing this claim.

---

> **"See Everything. Miss Nothing."**
>
> **— PHANTOM EYE 👁**
