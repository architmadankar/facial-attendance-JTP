from flask_restful import Resource, request
from modules.db import Session
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
        video = VideoModel.get_id(video_id)
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
        return {"message": "Video not found"}, 404
    
    @classmethod
    def frame(cls, cam):
        while True:
            frame = cam.get_frame()
            yield (
                    b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            )  

class VideoAdd(Resource):
    @classmethod
    
    def post(cls):
        video_json = request.get_json()
        video = video_schema.load(video_json, session=Session)
        try:
            video.create()
        except:
            return {"message": "An error occurred inserting the video"}, 500
        return video_schema.dump(video), 201
    

class VideoStop(Resource):
    @classmethod
    
    def get(cls, video_id: str):
        cam = VideoModel.get_id(video_id)
        if cam:
            App.stop(video_id)
            try:
                cam.is_active = False
                cam.create()
            except:
                return {"message": "An error occurred stopping the video"}, 500
            return {"message": "Video stopped successfully"}, 200
        return {"message": "Video not found"}, 404
    
class VideoStart(Resource):
    @classmethod
    
    def get(cls, video_id: str):
        cam = VideoModel.get_id(video_id)
        if cam:
            App.start(video_id)
            try:
                cam.is_active = True
                cam.create()
            except:
                return {"message": "An error occurred starting the video"}, 500
            return {"message": "Video started successfully"}, 200
        return {"message": "Video not found"}, 404
    
class VideoDelete(Resource):
    @classmethod
    
    def delete(cls, video_id: str):
        cam = VideoModel.get_id(video_id)
        if cam:
            cam.delete()
            return {"message": "Video deleted successfully"}, 200
        return {"message": "Video not found"}, 404