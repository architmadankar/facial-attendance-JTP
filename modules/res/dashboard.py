from flask_restful import Resource

class Dashboard(Resource):
    @classmethod
    def get(cls):
        user_id = None  
        if user_id:
            return {"message": "Dashboard"}, 200
        return {"message": "Not Logged In"}, 401