# import logging
from flask_restful import Resource
from modules.db import Session

from modules.models import AdminModel
from modules.schemas import AdminSchema
from flask import request

from flask_jwt_extended import create_refresh_token, create_access_token


admin_schema = AdminSchema()
class Admin(Resource):
    @classmethod
    def get(cls, admin_id: int):
        admin = AdminModel.get_id(admin_id)
        if not admin:
            return {"message": "Admin not found"}, 404
        return admin_schema.dump(admin), 200  
    @classmethod
    def delete(cls , admin_id: int):
        admin = AdminModel.get_id(admin_id)
        if not admin:
            return {"message": "Admin not found"}, 404
        admin.delete()
        return {"message": "Admin deleted successfully"}, 200
    
class AdminReg(Resource):
    @classmethod
    def post(cls):
        admin_json = request.get_json()
        admin = admin_schema.load(admin_json, session=Session)
        if AdminModel.get_username(admin.username):
            return {"message": "Admin already exists"}, 400
        admin.create()
        return {"message": "Admin Registered"}, 201
    
class AdminLogin(Resource):
    @classmethod
    def post(cls):
        admin_json = request.get_json()
        admin_data = admin_schema.load(admin_json, session=Session)
        admin = AdminModel.get_username(admin_data.username)
        if admin and admin.password == admin_data.password:
            access_token = create_access_token(identity=admin.id, fresh=True)
            refresh_token = create_refresh_token(identity=admin.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200
        return {"message": "Invalid credentials"}, 401

# class AdminLogin(Resource):
#     @classmethod
#     def post(cls):
#         logging.info("AdminLogin.post called")
#         admin_json = request.get_json()
#         logging.info(f"Received JSON: {admin_json}")
#         admin_data = admin_schema.load(admin_json, session=Session)
#         logging.info(f"Loaded admin data: {admin_data}")
#         admin = AdminModel.get_username(admin_data.username)
#         logging.info(f"Admin fetched from database: {admin}")
#         if admin and admin.password == admin_data.password:
#             logging.info("Admin logged in successfully")
#             return {"message": "Admin Logged in"}, 200
#         logging.warning("Invalid credentials")
#         return {"message": "Invalid credentials"}, 401