import os
from decouple import config

class AppConfig:
    DEBUG = config('DEBUG', default=True, cast=bool)
    PROPAGATE_EXCEPTIONS = True

FILE_ENCODING = os.path.join("clasifier", "encodings.pickle")
PATH_DATASET =  os.path.join("static", "images", "dataset")
MODEL_DLIB = "hog" #hog or cnn
DLIB_TOLERANCE = 0.6  # 0.6 -> default, 0.72 -> aggressive