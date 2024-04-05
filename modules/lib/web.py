from modules.lib.base_camera import BaseCamera
import cv2

class App(BaseCamera):
    camera_src = 0
    
    @classmethod
    def set_camera(cls, src):
        cls.camera_src = src
    
    @classmethod
    def fn_cap(cls):
        print("Capturing Image")
        pp = cv2.VideoCapture(cls.camera_src)
        
        if not pp.isOpened():
            print("Error: Camera not found")
        
        print("Checking Encodings [INFO]")
