import os
from decouple import config


class FlaskAppConfiguration:
    DEBUG = config('DEBUG', default=False, cast=bool)
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = config('SECRET_KEY')
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    UPLOADED_IMAGES_DEST = os.path.join("static", "images")


VIDEO_SOURCE = config('OPENCV_VIDEO', default=0, cast=int)

PATH_DATASET = os.path.join("static", "images", "dataset")
UNKNOWN_IMAGES_PATH = os.path.join("static", "images", "unknown")

HAAR_CASCADE_PATH = os.path.join("classifier", "haarcascade_frontalface_alt2.xml")


DLIB_MODEL = "hog"  # hog & cnn
DLIB_TOLERANCE = 0.6  # 0.6 -> default, 0.72 -> aggressive
ENCODINGS_FILE = os.path.join("db", "encodings.pickle")
