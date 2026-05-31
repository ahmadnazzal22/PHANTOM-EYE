from flask import Flask, render_template, Response, jsonify, request
import cv2
import threading
import os
from tracker import process_frame, load_known_faces, seen_persons, seen_plates

app = Flask(__name__)

current_frame = None
latest_detections = []
camera = None
is_running = False
lock = threading.Lock()

def gen_frames():
    global current_frame, latest_detections, camera, is_running
    while is_running and camera and camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            break
        processed, detections = process_frame(frame)
        with lock:
            latest_detections = detections
        ret2, buffer = cv2.imencode('.jpg', processed)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_camera', methods=['POST'])
def start_camera():
    global camera, is_running
    if not is_running:
        camera = cv2.VideoCapture(0)
        is_running = True
    return jsonify({"status": "started"})

@app.route('/start_video', methods=['POST'])
def start_video():
    global camera, is_running
    path = request.json.get("path", "")
    if os.path.exists(path):
        if camera:
            camera.release()
        camera = cv2.VideoCapture(path)
        is_running = True
        return jsonify({"status": "started", "file": path})
    return jsonify({"status": "error", "message": "File not found"}), 404

@app.route('/stop', methods=['POST'])
def stop():
    global camera, is_running
    is_running = False
    if camera:
        camera.release()
        camera = None
    return jsonify({"status": "stopped"})

@app.route('/detections')
def get_detections():
    with lock:
        return jsonify(latest_detections)

@app.route('/plates')
def get_plates():
    return jsonify(list(seen_plates))

@app.route('/faces')
def get_faces():
    files = os.listdir("detected_faces")
    return jsonify(files)

@app.route('/known_persons')
def get_known_persons():
    return jsonify(list(seen_persons))

@app.route('/reload_faces', methods=['POST'])
def reload_faces():
    load_known_faces()
    return jsonify({"status": "reloaded"})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)