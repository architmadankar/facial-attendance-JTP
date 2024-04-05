import cv2
import face_recognition
import pickle
from typing import Union
from datetime import date as d
from modules.settings import PATH_DATASET, HAAR_CASCADE_CLASSIFIER_PATH, FILE_ENCODING, MODEL_DLIB, DLIB_TOLERANCE
from modules.models import UserModel, MarkAttendanceModel
import os

class AppUtils:
    app_title = "Facial Attendace"

    def __init__(self, vid_input: Union[int, str]):
        self.vid_input = vid_input

    def chk(self):
        pp = cv2.VideoCapture(self.vid_input)
        while pp.isOpened():
            pe, frame = pp.read()
            if not pe:
                continue
            cv2.imshow(f"CAMERA_CHECK - {self.app_title}", frame)

            k = cv2.waitKey(100) & 0xFF
            if k == 27:
                break
        pp.release()
        cv2.destroyAllWindows()

    @classmethod
    def save_n_create(cls, name: str) -> str:
        user = UserModel(name=name)
        user.create()

        path_id = f"{PATH_DATASET}{os.sep}{user.id}"
        if not os.path.exists(path_id):
            os.makedirs(path_id)
        return path_id

    def check_n_snap(self):
        name = input("Enter User's Name: ")

        path_id = self.save_n_create(name)
        pp = cv2.VideoCapture(self.vid_input)
        haar_classifier = cv2.CascadeClassifier(HAAR_CASCADE_CLASSIFIER_PATH)
        inc = 0

        while True:
            pe, img = pp.read()
            if not pe:
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
            k = cv2.waitKey(100) & 0xFF
            if k == 27:
                break
            elif inc >= 15: #30 - number of images to be captured for dataset
                break

        pp.release()
        cv2.destroyAllWindows()

    def rec_n_attendance(self):
        print("Checking Encodings [INFO]")
        data = pickle.loads(open(FILE_ENCODING, "rb").read())

        print("Starting Attendance Capturing")
        pp = cv2.VideoCapture(self.vid_input)

        known_users = {}

        while True:
            pe, img = pp.read()

            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            r = img.shape[1] / float(rgb.shape[1])

            squares = face_recognition.face_locations(rgb, model=MODEL_DLIB)

            encodings = face_recognition.face_encodings(rgb, squares)
            names = []

            for encoding in encodings:
                matches = face_recognition.compare_faces(data["encodings"], encoding, DLIB_TOLERANCE)
                name_d = "Unknown"

                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    for i in matchedIdxs:
                        _id = data["ids"][i]
                        counts[_id] = counts.get(_id, 0) + 1

                    _id = max(counts, key=counts.get)
                    if _id:
                        if _id in known_users.keys():
                            user = known_users[_id]
                        else:
                            user = UserModel.get_id(_id)
                            known_users[_id] = user
                            if not MarkAttendanceModel.is_marked(d.today(), user):
                                user_attendance = MarkAttendanceModel(user=user)
                                user_attendance.create()
                        name_d = user.name
                names.append(name_d)
            for ((top, right, bottom, left), name_d) in zip(squares, names):
                if name_d == "Unknown":
                    continue
                top = int(top * r)
                right = int(right * r)
                bottom = int(bottom * r)
                left = int(left * r)
                top_left = (left, top)
                bottom_right = (right, bottom)

                cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(img, name_d, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

            cv2.imshow(f"Capturing Attendance - {self.app_title}", img)
            k = cv2.waitKey(100) & 0xFF
            if k == 27:
                break

        pp.release()
        cv2.destroyAllWindows()
        print("Attendance Marked Successfully!")
