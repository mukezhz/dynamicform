from os import environ
import json
from flask import request, jsonify
from api.model.user.operation import get_all_user, set_user


def index(id=None):
    if request.method == "GET":
        datas = get_all_user()
        # return the list of users after fetching the users from database
        return jsonify(datas)
    else:
        return jsonify({"message": "Method Not Implementd"}), 405


def create_user():
    if request.method == "POST":
        datas = json.loads(request.data)
        name = datas.get("name")
        address = datas.get("address")
        phone = datas.get("phone")
        email = datas.get("email")
        passwd = datas.get("password")
        # TODO: checking need to be done before data storage

        if set_user(
            name=name,
            address=address,
            phone=phone,
            email=email,
            password=passwd,
        ):
            return (jsonify({"message": "Account created successfully!!!"}), 201)
            # 201: Created
        else:
            return (
                jsonify({"message": "Error while value insertion!!!"}),
                400,
            )
            # 400: Bad Request
