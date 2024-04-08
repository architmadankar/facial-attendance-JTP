from flask_restful import Resource
from modules.schemas import VideoFeedSchema
from modules.models import VideoModel
from modules.lib.web import App
from flask import Response

video_list = VideoFeedSchema(many=True)
video_schema = VideoFeedSchema()
class VideoList(Resource):
    @classmethod
    def get(cls):
        return video_list.dump(VideoModel.find_all()), 200
    
class Video(Resource):
    @classmethod
    def get(cls, video_id: int):
        video = VideoModel.find_by_id(video_id)
        if video:
            return video_schema.dump(video), 200
        return {"message": "Video not found"}, 404

class VideoActive(Resource):
    @classmethod
    def get(cls, video_id: str):
        video = VideoModel.get_id(video_id)
        video_url = video.url
        cam = App
        if video_url == "0":
            video_url = 0
        elif video_url == "1":
            video_url = 1
        cam.set_camera(video_url)
        if video:
            resp = Response(cls.frame(cam(u_id=video_id)), mimetype='multipart/x-mixed-replace; boundary=frame')
            
        return resp
    @classmethod
    def frame(cls, cam):
        while True:
            frame = cam.get_frame()
            yield (
                    b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            )  
