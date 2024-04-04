import cv2
import face_recognition

import pickle

from typing import Union
from datetime import date as d

from modules.settings import PATH_DATASET, HAAR_CASCADE_CLASSIFIER_PATH, FILE_ENCODING, MODEL_DLIB, DLIB_TOLERANCE
from modules.models import User, MarkAttendance

import os

class AppUtils:
    app_title = "Facial Attendance"
    
    def __init__(self, vid_input: Union[int, str]):
        self.vid_input = vid_input
    
    def chk(self):
        pp=cv2.VideoCapture(self.vid_input)
        while pp.isOpened():
            pe, frame = pp.read()
            if not pe:
                continue
            cv2.imshow(f"CAMERA_CHECK - {self.app_title}", frame)
        
            k= cv2.waitKey(100) & 0xFF # ESC to quit
            if k == 27:
                break
        pp.release()
        cv2.destroyAllWindows()
        
    @classmethod
    def create_n_write(cls, name:str) -> str:
        user = User(name=name)
        user.create()
        path_id= f"{PATH_DATASET}{os.sep}{user.id}"
        if not os.path.exists(path_id):
            os.makedirs(path_id)
        return path_id
        
    def check_n_snap(self):
        name = input("Enter User's Name: ")
        path_id = self.create_n_write(name)
        pp = cv2.VideoCapture(self.vid_input)
        classifier_face = cv2.CascadeClassifier(HAAR_CASCADE_CLASSIFIER_PATH)
        inc = 0
        while True:
            pe, img = pp.read()
            if not pe:
                break
            face = classifier_face.detectMultiScale(img, 1.0485258, 6)
            
            for(x, y, w, h) in face:
                inc +=1
                cv2.imwrite(f"{path_id}{os.sep}{str(inc)}.jpg", img)
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imshow("Face Cropper - {self.app_title}", img)
                k = cv2.waitKey(30) & 0xFF
                if k == 27:
                    break
                elif inc >= 30:
                    break
        pp.release()
        cv2.destroyAllWindows()
        
    def rec_n_attendance(self):
        print("Loading Pickle Encoding File...")
        data = pickle.loads(open(FILE_ENCODING, "rb").read())
        print("Encoding File Loaded Successfully!")
        print("Starting Video Stream...")
        pp = cv2.VideoCapture(self.vid_input)
        known_users = {}
        while True:
            pe, img = pp.read()

            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            r = img.shape[1] / float(rgb.shape[1])
            
            faces = face_recognition.face_locations(rgb, model=MODEL_DLIB)
            encodings = face_recognition.face_encodings(rgb, faces)
            names = []
            
            for encoding in encodings:
                matches = face_recognition.compare_faces(data["encodings"], encoding, DLIB_TOLERANCE)
                name = "Unknown"
                
                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    for i in matchedIdxs:
                        _id = data["names"][i]
                        counts[_id] = counts.get(_id, 0) + 1
                    _id = max(counts, key=counts.get)
                    if _id:
                        if _id in known_users.keys():
                            user =known_users[_id]
                        else:
                            user = User.get_by_id(_id)
                            known_users[_id] = user
                                
                            if not MarkAttendance.is_marked(d.today(), user):
                                mark = MarkAttendance(user=user)
                                mark.create()
                                print(f"Attendance Marked for {user.name} on {d.today()}")
                        name = user.name
                names.append(name)
