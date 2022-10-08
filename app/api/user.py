# from crypt import methods
from urllib import response
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from datetime import datetime


from app.services.userService import addUserService

user_route = Blueprint(
    'user_route', 'user_route', url_prefix='/api/v1/user')

CORS(user_route)

@user_route.route("/add-user",methods=["POST"])
def addUser():
    post_data = request.get_json()
    try:
        first_name = post_data.get('first_name')
        last_name = post_data.get('last_name')
        email = post_data.get('email')
        password = post_data.get('password')


        addUserService(first_name,last_name,email,password)

        return jsonify({
            "success": "Successfully added."
        }),200
           
    except Exception as e:
        return jsonify({'error': str(e)}), 400