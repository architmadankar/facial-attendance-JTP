#similar to utils.py

from modules.lib.base_camera import BaseCamera
import cv2
import pickle
from modules.settings import DLIB_TOLERANCE, FILE_ENCODING
from modules.models import UserModel, MarkAttendanceModel
import numpy as np
import imutils
import face_recognition
from modules.settings import MODEL_DLIB
class App(BaseCamera):
    camera_src = 0
    this_rgb_frame = True
    @classmethod
    def set_camera(cls, src):
        cls.camera_src = src
    
    @classmethod
    def fn_cap(cls):
        print("Capturing Image")
        pp = cv2.VideoCapture(cls.camera_src)
        
        if not pp.isOpened():
            print("Camera not found [Error]")
        
        print("Checking Encodings [INFO]")
        data = pickle.loads(open(FILE_ENCODING, "rb").read())
        known_users = {}
        while True:
            pe, img = pp.read()
            
    @classmethod
    def rec_n_attendance(cls, fr: np.ndarray, data: dict, known_users: dict) -> bytes:
        rgb = cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)
        r_frame =imutils.resize(rgb, width=750)
        r= rgb.shape[1] / float(r_frame.shape[1])
        squares = []
        encodings = []
        names = []
        
        if cls.this_rgb_frame:
            squares = face_recognition.face_locations(rgb, model=MODEL_DLIB)
            encodings = face_recognition.face_encodings(rgb, squares)
            
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