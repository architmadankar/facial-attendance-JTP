import cv2
import face_recognition

import pickle

from typing import Union
from datetime import date as d

from modules.models import User

class AppUtils:
    app_title = "Facial Attendance"
    def __init__(self, vid_input: Union[int, str]):
        self.vid_input = vid_input
    
    def chk(self):
        x=cv2.VideoCapture(self.vid_input)
        while x.isOpened():
            y, frame = x.read()
            if not y:
                continue
            cv2.imshow(f"CAMERA_CHECK - {self.app_title}", frame)
        
            k= cv2.waitKey(100) & 0xFF # ESC to quit
            if k == 27:
                break
        x.release()
        cv2.destroyAllWindows()
        
        @classmethod
        def create_n_write(cls, name:str) -> str:
            user = User(name=name)
            user.create()
            