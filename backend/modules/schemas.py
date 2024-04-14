from typing import Union, Any, Optional, Mapping
from werkzeug.datastructures import FileStorage

from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from modules.models import AdminModel, UserModel, AttendanceModel, VideoModel


class AdminSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AdminModel
        load_only = ("password",) 
        dump_only = ("id",) 
        load_instance = True 


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        dump_only = ("id",) 
        load_instance = True 


class AttendanceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AttendanceModel
        dump_only = ("date", "user") 
        load_instance = True
    user = Nested(
        UserSchema
    )


class VideoFeedSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = VideoModel
        dump_only = ("is_active",)  
        load_instance = True


class FileStorageField(fields.Field):
    default_error_messages = {
        "invalid": "Not a valid image."
    }

    def _deserialize(self, value: Any, attr: Optional[str], data: Optional[Mapping[str, Any]], **kwargs) -> \
            Union[FileStorage, None]:
        if value is None:
            return None
        if not isinstance(value, FileStorage):
            self.fail("invalid") 
        return value


class ImageSchema(Schema):
    image = FileStorageField(required=True)
