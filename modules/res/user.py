import pickle
from flask_restful import Resource
from modules.db import Session
from modules.lib import image_helper
from modules.schemas import ImageSchema, UserSchema
from modules.models import UserModel
from flask import request
import os
import shutil
from flask_uploads import UploadNotAllowed
from modules.lib.train import ClassificationTrain

from modules.settings import FILE_ENCODING, PATH_DATASET
user_schema = UserSchema()
image_schema = ImageSchema()
class UserList(Resource):
    @classmethod
    def get(cls):
        return user_schema.dump(UserModel.find_all()), 200

class AddUser(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json, session=Session)
        try:
            user.create()
        except:
            return {"message": "User already exists"}, 500
        path_id = os.path.join(PATH_DATASET, str(user.id))
        if not os.path.exists(path_id):
            os.makedirs(path_id)
        return user_schema.dump(user), 201
    
class DeleteUser(Resource):
    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.get_id(user_id)
        if user:
            user.delete()
            path_id = os.path.join(PATH_DATASET, str(user_id))
            if os.path.exists(path_id):
                shutil.rmtree(path_id)
                
            ids=[]
            encodings=[]
            try:
                print("Reading encodings")
                data = pickle.loads(open(FILE_ENCODING, "rb").read())
                saved_encodings = data["encodings"]
                saved_ids = data["ids"]
                for i in range(len(saved_ids)):
                    if saved_ids[i] != user_id:
                        ids.append(saved_ids[i])
                        encodings.append(saved_encodings[i])
                data = {"ids": ids, "encodings": encodings}
                f = open(FILE_ENCODING, "wb")
                f.write(pickle.dumps(data))
                f.close()
            except FileNotFoundError:
                pass
            return {"message": "User deleted successfully"}, 200
        return {"message": "User not found"}, 404
    
class UserCap(Resource):
    @classmethod
    def psot(cls, user_id: int):
        data = image_schema.load(request.files)
        folder = os.path.join(PATH_DATASET, str(user_id)) #"dataset"
        filename = str(len(os.lisdir(os.path.join(PATH_DATASET, str(user_id))))+1)
        
        try:
            ext = image_helper.get_extension(data["image"].filename)
            save_path = filename + ext
            path_img = image_helper.save_image(data["image"], folder=folder, name=save_path)
            base_n = image_helper.get_extension(path_img)
        except UploadNotAllowed:
            ext = image_helper.get_extension(data["image"])
            return {"message": "Invalid file type"}, 400
        
        ClassificationTrain.training()
        return{"message": "Image saved"}, 201