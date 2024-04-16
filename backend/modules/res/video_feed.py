from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from modules.db import Session
from modules.models import VideoModel
from modules.schemas import VideoFeedSchema
from modules.lib.web import RecognitionCamera


video_feed_schema = VideoFeedSchema()
video_feed_list_schema = VideoFeedSchema(many=True)


class VideoFeedList(Resource):
    @classmethod
    def get(cls):
        return video_feed_list_schema.dump(VideoModel.find_all()), 200


class VideoFeed(Resource):
    @classmethod
    def get(cls, feed_id: str):
        video_feed = VideoModel.find_by_id(feed_id)

        if video_feed:
            return video_feed_schema.dump(video_feed), 200

        return {"message": 'Video feed not found'}, 404


class VideoFeedPreview(Resource):
    @classmethod
    def get(cls, feed_id: str):
        video_feed = VideoModel.find_by_id(feed_id)
        feed_url = video_feed.url
        camera_stream = RecognitionCamera
        if feed_url == "0":
            feed_url = 0
        elif feed_url == "1":
            feed_url = 1
        elif feed_url == "2":
            feed_url = 2
        elif feed_url == "3":
            feed_url = 3
        elif feed_url == "4":
            feed_url = 4
        camera_stream.set_video_source(feed_url)
        if video_feed:
            resp = Response(
                cls.gen_frame(camera_stream(unique_id=feed_id)),
                mimetype='multipart/x-mixed-replace; boundary=frame'
            )
            return resp

        return {"message": 'Video feed not found'}, 404

    @classmethod
    def gen_frame(cls, camera):
        while True:
            frame = camera.get_frame()
            yield (
                    b'--frame\r\n'
                    b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n'
            )


class VideoFeedAdd(Resource):
    @classmethod
    def post(cls):
        video_feed_json = request.get_json()

        video_feed = video_feed_schema.load(video_feed_json, session=Session)

        try:
            video_feed.create()
        except:
            return {"message": 'Error inserting'}, 500

        return video_feed_schema.dump(video_feed), 201


class VideoFeedStop(Resource):
    @classmethod
    def get(cls, feed_id: str):
        video_feed = VideoModel.find_by_id(feed_id)
        if video_feed:
            RecognitionCamera.stop(feed_id)
            try:
                video_feed.is_active = False
                video_feed.create()
            except:
                return {"message": 'Internal server error'}, 500
            return {"message": 'Video feed stopped'}, 200

        return {"message": 'Video feed not found'}, 404


class VideoFeedStart(Resource):
    @classmethod
    def get(cls, feed_id: str):
        video_feed = VideoModel.find_by_id(feed_id)
        if video_feed:
            try:
                video_feed.is_active = True
                video_feed.create()
            except:
                return {"message": 'Internal server error'}, 500
            return {"message": 'Video feed stopped'}, 200

        return {"message": 'Video feed not found'}, 404


class VideoFeedDelete(Resource):
    @classmethod
    def delete(cls, feed_id: str):
        video_feed = VideoModel.find_by_id(feed_id)
        if video_feed:
            video_feed.delete()
            return {"message": 'Video feed {} deleted'.format(video_feed.id)}, 200

        return {"message": 'Video feed not found'}, 404