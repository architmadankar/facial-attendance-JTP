from flask_restful import Resource

from modules.models import AttendanceModel
from modules.schemas import AttendanceSchema

attendance_list_schema = AttendanceSchema(many=True)


class AttendanceList(Resource):
    @classmethod
    def get(cls):
        return attendance_list_schema.dump(AttendanceModel.find_all()), 200
