from uuid import uuid4
from os import environ
import json
from flask import request, jsonify
from api.model.user.operation import (
    get_users,
    set_user,
    get_user_details,
    delete_user_details,
    update_user_details,
    select_password_from_email,
)


def index():
    if request.method == "GET":
        datas = get_users()
        if not datas:
            return jsonify({"message": "No any user exits!"})
        # return the list of users after fetching the users from database
        return jsonify(datas), 200
    else:
        return jsonify({"message": "Method Not Implementd"}), 405


def create_user():
    if request.method == "POST":
        userID = uuid4()
        datas = request.json
        name = datas.get("name")
        address = datas.get("address")
        phone = datas.get("phone")
        email = datas.get("email")
        password = datas.get("password")
        if not (userID and name and email and password):
            return jsonify({"message": "Information is insufficient!!!"})
        # TODO: checking need to be done before data storage

        if set_user(
            userID=userID,
            name=name,
            address=address,
            phone=phone,
            email=email,
            password=password,
        ):
            return (
                jsonify({"message": "Account created successfully!!!", "id": userID}),
                201,
            )
            # 201: Created
        else:
            return (
                jsonify({"message": "Duplicate field occurs!!!"}),
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


def update_user(id):
    if request.method == "PUT":
        datas = request.json
        name = datas.get("name")
        address = datas.get("address")
        phone = datas.get("phone")
        email = datas.get("email")
        # TODO: checking need to be done before data storage
        if update_user_details(
            userID=id,
            name=name,
            address=address,
            phone=phone,
            email=email,
        ):
            return (
                jsonify({"message": "User's detail successfully updated!!!", "id": id}),
                200,
            )
            # 201: Success
        else:
            return (
                jsonify({"message": "Error while value updation!!!"}),
                400,
            )
            # 400: Bad Request
