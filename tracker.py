import cv2
import numpy as np
from ultralytics import YOLO
import easyocr
import os
from datetime import datetime
import insightface
from insightface.app import FaceAnalysis

# ═══ تهيئة النماذج ═══
model = YOLO("yolov8n.pt")
ocr_reader = easyocr.Reader(['en'], gpu=False)

face_app = FaceAnalysis(providers=['CPUExecutionProvider'])
face_app.prepare(ctx_id=0, det_size=(320, 320))  # أصغر = أسرع

# ═══ مجلدات الحفظ ═══
os.makedirs("known_faces", exist_ok=True)
os.makedirs("detected_faces", exist_ok=True)
os.makedirs("detected_plates", exist_ok=True)

# ═══ متغيرات التتبع ═══
seen_persons = set()
seen_plates = set()
known_embeddings = []
known_names = []

# ═══ متغيرات السرعة ═══
frame_counter = 0
last_detections = []
last_annotated = None

# كاش للوجوه — ما نحلل نفس المنطقة مرتين
face_cache = {}
plate_cache = {}

def load_known_faces():
    global known_embeddings, known_names
    known_embeddings = []
    known_names = []
    for file in os.listdir("known_faces"):
        if file.endswith((".jpg", ".png")):
            img = cv2.imread(f"known_faces/{file}")
            if img is None:
                continue
            faces = face_app.get(img)
            if faces:
                known_embeddings.append(faces[0].embedding)
                known_names.append(os.path.splitext(file)[0])
    print(f"✅ Loaded {len(known_names)} known faces")

load_known_faces()

def identify_face(face_img):
    try:
        # تصغير الصورة قبل التحليل
        small = cv2.resize(face_img, (160, 160))
        faces = face_app.get(small)
        if not faces or not known_embeddings:
            return "Unknown"
        emb = faces[0].embedding
        sims = [np.dot(emb, k) / (np.linalg.norm(emb) * np.linalg.norm(k))
                for k in known_embeddings]
        best = np.argmax(sims)
        if sims[best] > 0.4:
            return known_names[best]
    except Exception:
        pass
    return "Unknown"

def read_plate(img_region):
    try:
        # تصغير منطقة اللوحة
        small = cv2.resize(img_region, (200, 60))
        results = ocr_reader.readtext(small)
        plate_text = ""
        for (_, text, conf) in results:
            if conf > 0.3:
                plate_text += text.strip().upper() + " "
        return plate_text.strip()
    except Exception:
        return ""

def get_region_key(x1, y1, x2, y2, grid=40):
    # مفتاح تقريبي للمنطقة — يتجاهل حركة صغيرة
    return (x1//grid, y1//grid, x2//grid, y2//grid)

def process_frame(frame):
    global frame_counter, last_detections, last_annotated

    frame_counter += 1

    # ═══ كل فريمين رجع النتيجة القديمة ═══
    if frame_counter % 2 != 0:
        if last_annotated is not None:
            return last_annotated, last_detections
        return frame, []

    # ═══ تصغير للتحليل ═══
    h, w = frame.shape[:2]
    scale = 640 / max(w, h)
    small_w, small_h = int(w * scale), int(h * scale)
    small_frame = cv2.resize(frame, (small_w, small_h))

    results = model(small_frame, conf=0.45, verbose=False)[0]
    annotated = frame.copy()
    detections = []

    for box in results.boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]
        conf = float(box.conf[0])

        # إرجاع الإحداثيات للحجم الأصلي
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        x1 = int(x1 / scale)
        y1 = int(y1 / scale)
        x2 = int(x2 / scale)
        y2 = int(y2 / scale)

        # تأكد من الحدود
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w, x2), min(h, y2)

        region = frame[y1:y2, x1:x2]
        if region.size == 0:
            continue

        is_new = True
        region_key = get_region_key(x1, y1, x2, y2)

        # ═══ شخص ═══
        if cls_name == "person":
            # استخدم الكاش إذا نفس المنطقة
            if region_key in face_cache:
                face_name = face_cache[region_key]
            else:
                face_name = identify_face(region)
                face_cache[region_key] = face_name
                # نظف الكاش إذا كبر
                if len(face_cache) > 30:
                    face_cache.clear()

            label = "PERSON: " + face_name.upper()

            if face_name != "Unknown":
                is_new = face_name not in seen_persons
                seen_persons.add(face_name)
            else:
                # احفظ الوجه المجهول كل 30 فريم بس
                if frame_counter % 30 == 0:
                    ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                    cv2.imwrite(f"detected_faces/face_{ts}.jpg", region)

            detections.append({
                "type": "person",
                "name": face_name,
                "confidence": round(conf, 2),
                "is_new": is_new
            })

        # ═══ سيارة ═══
        elif cls_name == "car":
            if region_key in plate_cache:
                plate_text = plate_cache[region_key]
            else:
                # OCR بس كل 10 فريمات
                if frame_counter % 10 == 0:
                    plate_text = read_plate(region)
                    plate_cache[region_key] = plate_text
                    if len(plate_cache) > 20:
                        plate_cache.clear()
                else:
                    plate_text = plate_cache.get(region_key, "")

            label = "CAR: " + plate_text if plate_text else "CAR"

            if plate_text:
                is_new = plate_text not in seen_plates
                seen_plates.add(plate_text)
                if is_new:
                    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                    cv2.imwrite(f"detected_plates/plate_{plate_text}_{ts}.jpg", region)

            detections.append({
                "type": "car",
                "plate": plate_text,
                "confidence": round(conf, 2),
                "is_new": is_new
            })

        # ═══ حيوان ═══
        elif cls_name in ["cat", "dog", "bird", "horse", "sheep",
                          "cow", "elephant", "bear", "zebra", "giraffe"]:
            label = "ANIMAL: " + cls_name.upper()
            detections.append({
                "type": "animal",
                "species": cls_name,
                "confidence": round(conf, 2),
                "is_new": True
            })

        # ═══ كائن آخر ═══
        else:
            label = cls_name.upper()
            detections.append({
                "type": "object",
                "name": cls_name,
                "confidence": round(conf, 2),
                "is_new": True
            })

        # ═══ رسم المستطيل الرئيسي ═══
        color = (0, 0, 255) if is_new else (255, 100, 0)
        cv2.rectangle(annotated, (x1, y1), (x2, y2), color, 3)

        # ═══ شريط العنوان فوق ═══
        text_scale = 1.0  # ← حجم النص (زود أو قلل)
        text_thick = 2
        padding_x = 14
        padding_y = 12

        (text_w, text_h), _ = cv2.getTextSize(
            label, cv2.FONT_HERSHEY_SIMPLEX, text_scale, text_thick
        )

        bar_x1 = x1
        bar_y1 = y1 - text_h - (padding_y * 2) - 6
        bar_x2 = x1 + text_w + (padding_x * 2)
        bar_y2 = y1 - 2

        # تأكد ما يطلع فوق الشاشة
        if bar_y1 < 0:
            bar_y1 = y2 + 2
            bar_y2 = y2 + text_h + (padding_y * 2) + 6

        # خلفية معتمة
        overlay = annotated.copy()
        cv2.rectangle(overlay, (bar_x1, bar_y1), (bar_x2, bar_y2), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.6, annotated, 0.4, 0, annotated)

        # إطار ملون
        cv2.rectangle(annotated, (bar_x1, bar_y1), (bar_x2, bar_y2), color, 2)

        # النص
        cv2.putText(annotated, label,
                    (bar_x1 + padding_x, bar_y2 - padding_y),
                    cv2.FONT_HERSHEY_SIMPLEX, text_scale,
                    (255, 255, 255), text_thick)
    # حفظ النتيجة للفريمات اللي ما اتحللت
    last_detections = detections
    last_annotated = annotated

    return annotated, detections