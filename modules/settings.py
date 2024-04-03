import os
from decouple import config

class AppConfig:
    DEBUG = config('DEBUG', default=True, cast=bool)
    PROPAGATE_EXCEPTIONS = True

#lib/train.py
FILE_ENCODING = os.path.join("classifier", "encodings.pickle")
PATH_DATASET =  os.path.join("static", "images", "dataset")
MODEL_DLIB = "hog" #hog or cnn
DLIB_TOLERANCE = 0.6  # 0.6 -> default, 0.72 -> aggressive

HAAR_CASCADE_CLASSIFIER_PATH = os.path.join("classifier", "haarcascade_frontalface_default.xml")