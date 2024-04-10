from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from flask_uploads import configure_uploads
from flask_restful import Api
from flask_cors import CORS
from marshmallow import ValidationError
from modules.lib.image_helper import IMAGE_SET

from modules.res.admin import Admin, AdminReg, AdminLogin
from modules.res.dashboard import Dashboard
from modules.res.mark import Mark
from modules.res.video import Video, VideoActive, VideoAdd, VideoList, VideoStop, VideoDelete, VideoStart
from modules.res.user import UserList, AddUser, UserCap, DeleteUser

app = Flask(__name__)
app.config.from_object("modules.settings.AppConfig")
api =Api(app)
configure_uploads(app, IMAGE_SET)
cors = CORS(app)
jwt = JWTManager(app)

@app.errorhandler(ValidationError)
def handle_validation(err):
    return jsonify(err.messages), 400

api.add_resource(VideoList, "/videos")
api.add_resource(VideoAdd, "/video/add")
api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(VideoActive, "/video/active/<string:video_id>")
api.add_resource(VideoStop, "/video/stop/<string:video_id>")
api.add_resource(VideoStart, "/video/start/<string:video_id>")
api.add_resource(VideoDelete, "/video/delete/<string:video_id>")

api.add_resource(Admin, "/admin/<int:admin_id>")
api.add_resource(AdminReg, "/admin/signup")
api.add_resource(AdminLogin, "/admin/login")

api.add_resource(UserList, "/user/<int:user_id>")
api.add_resource(AddUser, "/user/add")
api.add_resource(UserCap, "/user/cap/<int:user_id>")
api.add_resource(DeleteUser, "/user/delete/<int:user_id>")

api.add_resource(Dashboard, "/dashboard")
api.add_resource(Mark, "/attendance")
