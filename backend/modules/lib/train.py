import os
import pickle

import cv2
import face_recognition

from modules.settings import PATH_DATASET, ENCODINGS_FILE, DLIB_MODEL


class TrainClassifier:
    @classmethod
    def train(cls):
        try:
            print("loading encoding.pickle file")
            with open(ENCODINGS_FILE, "rb") as ef:
                data = pickle.loads(ef.read())
            known_encodings = data["encodings"]
            known_ids = data["ids"]
        except FileNotFoundError:
            known_encodings = []
            known_ids = []

        unq_ids = [int(_id) for _id in set(known_ids)]

        path_id = [os.path.join(PATH_DATASET, f) for f in os.listdir(PATH_DATASET)]

        for path_id in path_id:
            _id = int(os.path.split(path_id)[1])
            if _id in unq_ids:
                continue
            path_images = [os.path.join(path_id, f) for f in os.listdir(path_id)]
            for i, path_image in enumerate(path_images):
                print(f" ID: {_id}, creating pickle with image  {i + 1}/{len(path_images)}")
                image = cv2.imread(path_image)
                try:
                    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                except cv2.error:
                    try:
                        os.remove(path_image)
                    except (FileNotFoundError, PermissionError):
                        pass
                    continue

                face_box = face_recognition.face_locations(rgb, model=DLIB_MODEL)
                encodings = face_recognition.face_encodings(rgb, face_box)
                for encoding in encodings:
                    known_encodings.append(encoding)
                    known_ids.append(_id)

        print(" serializing -- saving to file...")
        data = {"encodings": known_encodings, "ids": known_ids}
        f = open(ENCODINGS_FILE, "wb")
        f.write(pickle.dumps(data))
        f.close()