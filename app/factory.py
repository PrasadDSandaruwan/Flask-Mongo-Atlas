
import os

from flask import Flask
from flask.json import JSONEncoder
from flask_cors import CORS


from bson import json_util, ObjectId
from datetime import datetime

import configparser

from app.api.test_routes import route_test



config = configparser.ConfigParser()

config.read(os.path.abspath(os.path.join(".ini")))

class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['MONGO_URI'] = config["TEST"]["DB_URI"]

    app.json_encoder = MongoJsonEncoder
    app.register_blueprint(route_test)

    return app


