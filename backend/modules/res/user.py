import os
import shutil
import pickle

from flask import request
from flask_restful import Resource
from flask_uploads import UploadNotAllowed

from modules.db import Session
from modules.lib import image_helper
from modules.lib.train_classifier import TrainClassifier
from modules.models import UserModel
from modules.schemas import UserSchema, ImageSchema
from modules.settings import PATH_DATASET, ENCODINGS_FILE


user_schema = UserSchema()
user__list_schema = UserSchema(many=True)
image_schema = ImageSchema()


class UserList(Resource):
    @classmethod
    def get(cls):
        return user__list_schema.dump(UserModel.find_all()), 200

class UserAdd(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()

        user = user_schema.load(user_json, session=Session)

        try:
            user.create()
        except:
            return {"message": "Error inserting the user data."}, 500

        path_id = os.path.join(PATH_DATASET, str(user.id))
        if not os.path.exists(path_id):
            os.makedirs(path_id)

        return user_schema.dump(user), 201


class UserDelete(Resource):
    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if user:
            user.delete()
            path_id = os.path.join(PATH_DATASET, str(user_id))
            if os.path.exists(path_id):
                shutil.rmtree(path_id)
            ids = []
            encodings = []
            try:
                print("[INFO] loading encodings...")
                data = pickle.loads(open(ENCODINGS_FILE, "rb").read())
                known_encodings = data["encodings"]
                known_ids = data["ids"]
                for index in range(len(known_ids)):
                    if known_ids[index] != user_id:
                        ids.append(known_ids[index])
                        encodings.append(known_encodings[index])
                data = {"encodings": encodings, "ids": ids}
                f = open(ENCODINGS_FILE, "wb")
                f.write(pickle.dumps(data))
                f.close()
            except FileNotFoundError:
                pass
            return {"message": f"User {user.name} with id {user.id} deleted."}, 200

        return {"message": "User not found."}, 404


class UserCapture(Resource):
    @classmethod
    def post(cls, user_id: int):
        data = image_schema.load(request.files)
        folder = os.path.join("dataset", str(user_id))
        filename = str(len(os.listdir(os.path.join(PATH_DATASET, str(user_id)))) + 1)
        try:
            extension = image_helper.get_extension(data["image"].filename)
            save_as_filename = filename + extension
            image_path = image_helper.save_image(data["image"], folder=folder, name=save_as_filename)
            basename = image_helper.get_basename(image_path)
        except UploadNotAllowed:
            extension = image_helper.get_extension(data["image"])
            return {"message": f"Image has illegal extension: {extension}"}, 400

        TrainClassifier.train()
        return {"message": f"Image {basename} uploaded."}, 201