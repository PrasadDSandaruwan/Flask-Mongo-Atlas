from flask import Blueprint, request, jsonify
from flask_cors import CORS
from datetime import datetime


route_test = Blueprint(
    'route_test', 'route_test', url_prefix='/api/v1/')

CORS(route_test)

@route_test.route('/', methods=['GET'])
def api_test_get():
    response = {
        "Message": "Hellow World"
    }
    return jsonify(response)



