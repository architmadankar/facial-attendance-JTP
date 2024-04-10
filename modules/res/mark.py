from flask_restful import Resource
from modules.models import MarkAttendanceModel
from modules.schemas import AttendanceSchema
from flask_jwt_extended import jwt_required

attendance_list_schema = AttendanceSchema(many=True)


class Mark(Resource):
    @classmethod
    @jwt_required
    def get(cls):
        return attendance_list_schema.dump(MarkAttendanceModel.find_all()), 200