import os
from decouple import config

class AppConfig:
    DEBUG = config('DEBUG', default=True, cast=bool)
    PROPAGATE_EXCEPTIONS = True
    UPLOADED_IMAGES_DEST = os.path.join("static", "images")


#lib/train.py
FILE_ENCODING = os.path.join("classifier", "encodings.pickle")
PATH_DATASET =  os.path.join("static", "images", "dataset")
MODEL_DLIB = "hog" #hog or cnn
DLIB_TOLERANCE = 0.6  # 0.6 -> default, 0.72 -> aggressive

HAAR_CASCADE_CLASSIFIER_PATH = os.path.join("classifier", "haarcascade_frontalface_default.xml")

CAMERA_SOURCE = config('OPENCV_VIDEO', default=0, cast=int)
UNKNOWN_IMAGES_PATH = os.path.join("static", "images", "unknown")
