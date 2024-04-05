from flask_restful import Resource
from modules.db import Session
from modules.models import AdminModel
from modules.schemas import AdminSchema
from flask import request
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
        admin = admin_schema.loada(admin_json, session=Session)
        if AdminModel.get_username(admin.username):
            return {"message": "Admin already exists"}, 400
        admin.save()
        return {"message": "Admin Registered"}, 201
    
class AdminLogin(Resource):
    @classmethod
    def post(cls):
        pass
