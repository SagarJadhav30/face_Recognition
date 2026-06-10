import csv
from datetime import datetime
from pathlib import Path

import cv2
import face_recognition  # type: ignore[import-not-found]
import numpy as np
  

def load_face_encoding(image_path: Path, label: str): 
    image = face_recognition.load_image_file(str(image_path))
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        raise ValueError(f"No face found in {image_path}")
    return encodings[0]


video_capture = cv2.VideoCapture(0) 
if not video_capture.isOpened():
    raise RuntimeError("Could not open the webcam.")

photo_dir = Path("photos")
known_people = [
    ("jobs", [photo_dir / "jobs.jpeg", photo_dir / "jobs.jpg"]),
    ("ratan tata", [photo_dir / "tata.jpg"]),
    ("sadmona", [photo_dir / "sadmona.jpg"]),
    ("tesla", [photo_dir / "tesla.jpeg", photo_dir / "tesla.jpg"]),
]

known_face_encodings = []
known_faces_names = []

for name, image_candidates in known_people:
    image_path = next((candidate for candidate in image_candidates if candidate.exists()), None)
    if image_path is None:
        raise FileNotFoundError(f"Missing image for {name}: {', '.join(str(candidate) for candidate in image_candidates)}")

    known_face_encodings.append(load_face_encoding(image_path, name))
    known_faces_names.append(name)

students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

current_date = datetime.now().strftime("%Y-%m-%d")

with open(current_date + ".csv", "w", newline="") as f:
    lnwriter = csv.writer(f)

    try:
        while True:
            success, frame = video_capture.read()
            if not success or frame is None:
                raise RuntimeError("Failed to read a frame from the webcam.")

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

            if s:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame,
                    face_locations,
                    num_jitters=0,
                )

                face_names = []

                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(
                        known_face_encodings,
                        face_encoding,
                    )

                    name = ""
                    face_distance = face_recognition.face_distance(
                        known_face_encodings,
                        face_encoding,
                    )

                    best_match_index = np.argmin(face_distance)

                    if matches[best_match_index]:
                        name = known_faces_names[best_match_index]

                    face_names.append(name)

                    if name in known_faces_names and name in students:
                        students.remove(name)
                        print(students)

                        current_time = datetime.now().strftime("%H-%M-%S")
                        lnwriter.writerow([name, current_time])

            cv2.imshow("Attendance System", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        video_capture.release()
        cv2.destroyAllWindows()
