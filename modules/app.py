from flask import Flask, jsonify

from flask_uploads import configure_uploads
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object("modules.settings.AppConfig")
api =Api(app)
configure_uploads(app, IMAGE_X)

cors = CORS(app)

