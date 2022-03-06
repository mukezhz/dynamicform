from uuid import uuid4
from os import environ
import json
from flask import request, jsonify
from api.model.user.operation import (
    get_users,
    set_user,
    get_user_details,
    delete_user_details,
)


def index():
    if request.method == "GET":
        datas = get_users()
        # return the list of users after fetching the users from database
        return jsonify(datas), 200
    else:
        return jsonify({"message": "Method Not Implementd"}), 405


def create_user():
    if request.method == "POST":
        userID = uuid4()
        datas = json.loads(request.data)
        name = datas.get("name")
        address = datas.get("address")
        phone = datas.get("phone")
        email = datas.get("email")
        passwd = datas.get("password")
        # TODO: checking need to be done before data storage

        if set_user(
            userID=userID,
            name=name,
            address=address,
            phone=phone,
            email=email,
            password=passwd,
        ):
            return (
                jsonify({"message": "Account created successfully!!!", "id": userID}),
                201,
            )
            # 201: Created
        else:
            return (
                jsonify({"message": "Error while value insertion!!!"}),
                400,
            )
            # 400: Bad Request


def get_user(id):
    if request.method == "GET":
        return jsonify(get_user_details(id=id))
    else:
        return jsonify({"message": "Invalid id has been provided"}), 400


def delete_user(id):
    if request.method == "DELETE" and delete_user_details(id=id):
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "Invalid id has been provided"}), 400
