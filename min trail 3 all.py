import cv2
import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import mysql.connector
import numpy as np

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR PASSWORD",
        database="YOUR DATABASE"
    )

def get_face_image(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT image FROM known_faces WHERE name = %s", (name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return cv2.imdecode(np.frombuffer(result[0], np.uint8), cv2.IMREAD_COLOR)
    else:
        print(f"No face found for: {name}")
        return None

def alert_stranger():
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("Stranger Alert", "A stranger has been detected!")
    root.destroy()

def detect_and_recognize(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_detector.detectMultiScale(gray_frame, 1.3, 5)
    for (x, y, w, h) in detected_faces:
        face_roi = frame[y:y+h, x:x+w]
        label = "Unknown"
        for person, known_img in database_faces.items():
            if known_img is not None:
                resized_img = cv2.resize(known_img, (w, h))
                if cv2.norm(resized_img, face_roi, cv2.NORM_L2) < 300:
                    label = person
                    break
        if label == "Unknown":
            playsound("C:\\Users\\barat\\Downloads\\ALARM.mp3")
            alert_stranger()
            cv2.putText(frame, "STRANGER ALERT!", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 5)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face_detector.empty():
    print("Failed to load face detector.")
    exit()

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Cannot access webcam.")
    exit()

database_faces = {
    "BARATH": get_face_image("BARATH")
}

while True:
    ret, live_frame = camera.read()
    if not ret:
        print("Frame capture failed.")
        break
    output_frame = detect_and_recognize(live_frame)
    cv2.imshow("Face Recognition", output_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
