from os import environ
from datetime import datetime, timedelta
from flask import request, make_response, jsonify
from werkzeug.security import check_password_hash
from api.model.user.operation import (
    select_user_password_token_using_email,
    update_user_token,
    get_all_from_token,
)
from api.controller.user import create_user as register
from api.utils.token import encode_jwt, verify_token
from api.controller.user import set_user


def login():
    if request.method == "POST":
        datas = request.json
        email = datas.get("email")
        password = datas.get("password")
        if not (email and password):
            return jsonify({"message": "Email and password is not provided!!!"})
        infos = select_user_password_token_using_email(email)
        userID = infos.get("id")
        pwhash = infos.get("password")
        refresh_token = infos.get("token")
        if not check_password_hash(pwhash, password):
            return jsonify({"message": "Email and password didn't match!!!"})

        access_token = request.cookies.get("access_token")
        payload = {"email": email, "userID": userID, "password": pwhash}

        if not access_token:
            # jwt for obtaining access token
            headers = {"exp": str(datetime.utcnow() + timedelta(days=1))}
            token_secret = environ.get("JWT_SECRET")
            access_token = encode_jwt(headers, payload, token_secret)

        if not refresh_token:
            # jwt for obtaining refresh token
            print("obtaining jwt token")
            headers = {"exp": str(datetime.utcnow() + timedelta(days=30))}
            refresh_secret = environ.get("JWT_REFRESH_SECRET")
            refresh_token = encode_jwt(headers, payload, refresh_secret)
            if not update_user_token(email=email, token=refresh_token):
                return jsonify({"message": "Error while updating refresh token!!!"})
        response = {
            "message": "User logged in successfully!!!",
            "access_token": "Has been to to your cookie!!!",
            "refresh_token": refresh_token,
        }

        if not (refresh_token and access_token):
            response = {
                "message": "Invalid credentials!!!",
            }

        resp = make_response(jsonify(response))
        resp.set_cookie(
            key="access_token",
            value=access_token,
            max_age=60 * 60 * 24,
            httponly=True,
        )
        return resp


def logout():
    refresh_secret = environ.get("JWT_REFRESH_SECRET")
    if request.method == "POST":
        refresh_token = request.json.get("refresh_token")
        email = request.json.get("email")
        data = verify_token(refresh_token, key=refresh_secret)
        if email == data.get("email"):
            return jsonify(
                {"message": "Invalid email didn't match with refresh token!!!"}
            )
        if not (refresh_token and email):
            return jsonify({"message": "Refresh token or email not provided!!!"})
        refresh_token = ""
        if not update_user_token(email=email, token=refresh_token):
            return jsonify({"message": "Error while updating refresh token!!!"})
        response = {"message": "Logout sucessful!!!"}
        resp = make_response(jsonify(response))
        resp.delete_cookie(key="access_token")
        return resp


def token():
    refresh_secret = environ.get("JWT_REFRESH_SECRET")
    access_secret = environ.get("JWT_SECRET")
    if request.method == "POST":
        refresh_token = request.json.get("refresh_token")
        if not refresh_token:
            return jsonify({"message": "Refresh Token is not provided!!!"})
        data = verify_token(refresh_token, key=refresh_secret)
        if not data:
            return jsonify({"message": "Invalid refresh token!!!"})
        if not get_all_from_token(refresh_token):
            return jsonify({"message": "Invalid token!!!"})
        headers = {"exp": str(datetime.utcnow() + timedelta(days=1))}
        payload = data
        access_token = encode_jwt(headers, payload, access_secret)
        response = {"message": "Access token is refeshed successfully!!!"}
        if not (refresh_token and access_token):
            response = {
                "message": "Error in token!!!",
            }

        resp = make_response(jsonify(response))
        resp.set_cookie(
            key="access_token",
            value=access_token,
            max_age=60 * 60 * 24,
            httponly=True,
        )
        return resp
