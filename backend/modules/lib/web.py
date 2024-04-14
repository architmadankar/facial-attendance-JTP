import pickle
from typing import Dict
from datetime import date as dt

import cv2
import imutils
import numpy as np
import face_recognition

from modules.settings import (
    DLIB_MODEL, DLIB_TOLERANCE,
    ENCODINGS_FILE
)
from modules.lib.base_camera import BaseCamera
from modules.models import UserModel, AttendanceModel


class RecognitionCamera(BaseCamera):
    src = 0
    process_this_frame = True

    @classmethod
    def set_video_source(cls, source):
        cls.src = source

    @classmethod
    def frames(cls):
        print("[INFO] starting Camera ...")
        camera = cv2.VideoCapture(cls.src)

        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        print("[INFO] loading encodings...")
        data = pickle.loads(open(ENCODINGS_FILE, "rb").read())

        known_users = {}
        while True:
            _, img = camera.read()
            yield cls.markAttendance(img, data, known_users)

    @classmethod
    def markAttendance(cls, frame: np.ndarray, data: Dict, known_users: Dict) -> bytes:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = imutils.resize(rgb_frame, width=750)
        r = frame.shape[1] / float(rgb.shape[1])

        face_box = []
        encodings = []
        names = []

        if cls.process_this_frame:
            face_box = face_recognition.face_locations(rgb, model=DLIB_MODEL)

            encodings = face_recognition.face_encodings(rgb, face_box)

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
                        if _id in known_users.keys():
                            user = known_users[_id]
                        else:
                            user = UserModel.find_by_id(_id)
                            known_users[_id] = user
                            if not AttendanceModel.is_marked(dt.today(), user):
                                student_attendance = AttendanceModel(user=user)
                                student_attendance.create()
                        display_name = user.name
                names.append(display_name)
        cls.process_this_frame = not cls.process_this_frame
        for ((top, right, bottom, left), display_name) in zip(face_box, names):
            if display_name == "Unknown":
                continue
            top = int(top * r)
            right = int(right * r)
            bottom = int(bottom * r)
            left = int(left * r)
            top_left = (left, top)
            bottom_right = (right, bottom)

            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, display_name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        return cv2.imencode('.jpg', frame)[1].tobytes()