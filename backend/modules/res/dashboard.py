from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

class Dashboard(Resource):
    @classmethod
    @jwt_required(optional=True)
    def get(cls):
        user_id = get_jwt_identity()
        if user_id:
            return {'message': 'You are logged in.'}, 200
        return {'message': 'Login to continue.'}, 401