from typing import Any, Mapping, Union
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from modules.models import VideoModel, Admin, User, MarkAttendance
from werkzeug.datastructures import FileStorage

class AdminSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Admin
        load_instance = True
        load_only = ("passwd",)
        dunp_only = ("id",)
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        dump_only = ("id",)
class MarkAttendanceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MarkAttendance
        load_instance = True
        dump_only = ("date","user_id")
    user_id = Nested(UserSchema)
class VideoModelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = VideoModel
        load_instance = True
        dump_only = ("is_active",)
        
class FileSchema(fields.Field):
    error_msg = {"invalid": "Not a valid img file"}
    def _deserialize(self, value: Any, attr: str | None, data: Mapping[str, Any] | None, **kwargs) -> Union[FileStorage, None]:
        if value is None:
            return None
        if not isinstance(value, FileStorage):
            self.fail("invalid")
        return value
        
class ImageSchema(Schema):
    img = FileSchema(required=True)