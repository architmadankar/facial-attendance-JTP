import os
import cv2
import face_recognition

import pickle

#KNN Classifier Training and storing results
class ClassificationTrain:
    #using decorator to sk
    @classmethod
    def training(cls):
        try:
            print("Checking Encodings [INFO]")
            with open(FILE_ENCODING, "rb") as x: #file path
                data = pickle.loads(x.read())
                #init recognized encodings and names
                rec_encodings = data["encodings"]
                rec_ids = data["ids"]
        except FileNotFoundError:
            rec_encodings = []
            rec_ids = []
            #converting _id into int and set
        unq_id =  [int(_id) for _id in set(rec_ids)]
        path_id = [os.path.join(PATH_DATASET, f) for f in os.listdir(PATH_DATASET)]
        
        for path_of_id in path_id:
            _id = int(os.path.split(path_id[1]))
            if _id in unq_id:
                continue
            path_img = [os.path.join(path_of_id, f) for f in os.listdir(path_of_id)]
            for i,path_of_img in enumerate(path_img):
                print(f"ID: {_id}, processing_image {i+1}/{len(path_img)}")
                image=cv2.imread(path_of_img)
                try:
                    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                except cv2.error:
                    
                    try:
                        os.remove(path_of_img)
                    except (FileNotFoundError, PermissionError):
                        pass
                    continue
                #detect coords of box
                squares = face_recognition.face_locations(rgb, model=MODEL_DLIB)
                encs = face_recognition.face_encodings(rgb, squares)
                for enc in encs:
                    rec_encodings.append(enc)
                    rec_ids.append(_id)
                    
        print("Encoding_Serialize")
        data = {"encs": rec_encodings, "ID": rec_ids}
        f=open(FILE_ENCODING, "wb")
        f.write(pickle.dumps(data))
        f.close()
                    
                    