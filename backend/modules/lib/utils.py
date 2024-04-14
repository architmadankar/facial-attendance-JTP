import os
import pickle
from typing import Union
from datetime import date as dt

import cv2
import face_recognition

from modules.models import UserModel, AttendanceModel
from modules.settings import (
    PATH_DATASET as DATASET_PATH,
    HAAR_CASCADE_PATH,
    DLIB_MODEL, DLIB_TOLERANCE, ENCODINGS_FILE
)


class AppUtils:
    app_title = "Attendance System"

    def __init__(self, input_video: Union[int, str]):
        self.input_video = input_video

    def chk(self):
        cap = cv2.VideoCapture(self.input_video)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:  
                continue
            cv2.imshow(f"Checking Camera - {self.app_title}", frame)

            k = cv2.waitKey(100) & 0xff  
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

    @classmethod
    def save_n_create(cls, name: str) -> str:
        user = UserModel(name=name)
        user.create()

        path_id = f"{DATASET_PATH}{os.sep}{user.id}"
        if not os.path.exists(path_id):
            os.makedirs(path_id)
        return path_id

    def detect_cap(self):
        name = input("Enter Student's Name: ")

        path_id = self.save_n_create(name)
        cap = cv2.VideoCapture(self.input_video)
        haar_classifier = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
        inc = 0

        while True:
            ret, img = cap.read()
            if not ret: 
                break
            faces = haar_classifier.detectMultiScale(img, 1.0485258, 6)

            for(x, y, w, h) in faces:
                inc += 1

                cv2.imwrite(
                    f"{path_id}{os.sep}{str(inc)}.jpg",
                    img
                )  
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imshow(f"Capturing Face - {self.app_title}", img)
            k = cv2.waitKey(100) & 0xff  
            if k == 27:
                break
            elif inc >= 15:  
                break

        cap.release()
        cv2.destroyAllWindows()

    def markAttendance(self):
        print("[INFO] loading encodings...")
        data = pickle.loads(open(ENCODINGS_FILE, "rb").read())

        print("[INFO] starting video stream...")
        cap = cv2.VideoCapture(self.input_video)

        known_students = {}

        while True:
            ret, img = cap.read()

            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            r = img.shape[1] / float(rgb.shape[1])

            face_box = face_recognition.face_locations(rgb, model=DLIB_MODEL)

            encodings = face_recognition.face_encodings(rgb, face_box)
            names = []

            for encoding in encodings:
                matches = face_recognition.compare_faces(data["encodings"], encoding, DLIB_TOLERANCE)
                display_name = "Unknown"

                if True in matches:
                    matched_indexes = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    for matched_index in matched_indexes:
                        _id = data["ids"][matched_index]
                        counts[_id] = counts.get(_id, 0) + 1

                    _id = max(counts, key=counts.get)
                    if _id:
                        if _id in known_students.keys():
                            user = known_students[_id]
                        else:
                            user = UserModel.find_by_id(_id)
                            known_students[_id] = user
                            if not AttendanceModel.is_marked(dt.today(), user):
                                student_attendance = AttendanceModel(user=user)
                                student_attendance.create()
                        display_name = user.name
                names.append(display_name)

            for ((top, right, bottom, left), display_name) in zip(face_box, names):
                if display_name == "Unknown":
                    continue
                top = int(top * r)
                right = int(right * r)
                bottom = int(bottom * r)
                left = int(left * r)
                top_left = (left, top)
                bottom_right = (right, bottom)

                cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(img, display_name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

            cv2.imshow(f"Recognizing Faces - {self.app_title}", img)
            k = cv2.waitKey(100) & 0xff  
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
        print("Attendance Successful!")