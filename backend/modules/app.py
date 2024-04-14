from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_uploads import configure_uploads
from marshmallow import ValidationError

from modules.lib.image_helper import IMAGE_SET
from modules.res.dashboard import Dashboard
from modules.res.admin import Admin, AdminRegister, AdminLogin
from modules.res.user import UserList, UserAdd, UserCapture, UserDelete
from modules.res.attendance import AttendanceList
from modules.res.video_feed import (
    VideoFeedList, VideoFeedAdd, VideoFeed, VideoFeedPreview, VideoFeedStop, VideoFeedStart, VideoFeedDelete
)


app = Flask(__name__)
app.config.from_object("modules.settings.FlaskAppConfiguration")
api = Api(app)
configure_uploads(app, IMAGE_SET)
jwt = JWTManager(app)
cors = CORS(app)


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


api.add_resource(Admin, "/admin/<int:admin_id>")
api.add_resource(AdminRegister, "/admin/register")
api.add_resource(AdminLogin, "/admin/login")

api.add_resource(Dashboard, "/dashboard")

api.add_resource(VideoFeedList, "/video")
api.add_resource(VideoFeedAdd, "/video/add")
api.add_resource(VideoFeed, "/video/<string:feed_id>")
api.add_resource(VideoFeedPreview, "/video/preview/<string:feed_id>")
api.add_resource(VideoFeedStop, "/video/stop/<string:feed_id>")
api.add_resource(VideoFeedStart, "/video/start/<string:feed_id>")
api.add_resource(VideoFeedDelete, "/video/delete/<string:feed_id>")

api.add_resource(UserList, "/users")
api.add_resource(UserAdd, "/users/add")
api.add_resource(UserCapture, "/users/cap/<int:user_id>")
api.add_resource(UserDelete, "/users/delete/<int:user_id>")

api.add_resource(AttendanceList, "/attendance")
