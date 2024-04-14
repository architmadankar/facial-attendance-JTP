from flask_restful import Resource
from flask import request
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

from modules.db import Session
from modules.models import AdminModel
from modules.schemas import AdminSchema

admin_schema = AdminSchema()


class Admin(Resource):
    @classmethod
    def get(cls, admin_id: int):
        admin = AdminModel.find_by_id(admin_id)
        if not admin:
            return {"message": "Admin not found"}, 404

        return admin_schema.dump(admin), 200

    @classmethod
    def delete(cls, admin_id: int):
        admin = AdminModel.find_by_id(admin_id)
        if not admin:
            return {"message": "Admin not found"}, 404

        admin.delete()
        return {"message": "Admin deleted"}, 200


class AdminRegister(Resource):
    @classmethod
    def post(cls):
        admin_json = request.get_json()
        admin = admin_schema.load(admin_json, session=Session)

        if AdminModel.find_by_username(admin.username):
            return {"message": "Admin username exists"}, 400

        admin.create()

        return {"message": "Admin registered"}, 201


class AdminLogin(Resource):
    @classmethod
    def post(cls):
        admin_json = request.get_json()
        admin_data = admin_schema.load(admin_json, session=Session)

        admin = AdminModel.find_by_username(admin_data.username)

        if admin and safe_str_cmp(admin.password, admin_data.password):
            access_token = create_access_token(identity=admin.id, fresh=True)
            refresh_token = create_refresh_token(admin.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        return {"message": "Invalid credentials"}, 401