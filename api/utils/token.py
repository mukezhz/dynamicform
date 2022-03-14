from flask import request, jsonify
from os import environ
from functools import wraps
import jwt
from api.model.user.operation import select_user_password_token_using_email
from api.model.merge.userform import select_all_from_userid


def encode_jwt(headers, payload, secret):
    token = jwt.encode(payload=payload, key=secret, headers=headers, algorithm="HS256")
    return token


def verify_token(encoded, key=None, algorithms=["HS256"]):
    try:
        data = jwt.decode(encoded, key=key, algorithms=algorithms)
    except jwt.exceptions.InvalidSignatureError:
        return None
    return data


def token_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        token = request.cookies.get("access_token")
        # if "x-access-tokens" in request.headers:
        #     token = request.headers["x-access-tokens"]

        if not token:
            return jsonify({"message": "A valid token is missing!!!"}), 403
        data = verify_token(token, key=environ.get("JWT_SECRET"))
        email = data.get("email")
        userID = data.get("userID")
        current_user = select_user_password_token_using_email(email)
        # password = current_user.get("password")
        if not (data and current_user and email and userID):
            return jsonify({"message": "Unauthorized user token is invalid!!!"}), 403
        return func(userID)

    return decorator


def verify_user(func):
    @wraps(func)
    def decorator(formID=None):
        token = request.cookies.get("access_token")
        # if "x-access-tokens" in request.headers:
        #     token = request.headers["x-access-tokens"]

        if not token:
            return jsonify({"message": "A valid token is missing!!!"}), 403
        data = verify_token(token, key=environ.get("JWT_SECRET"))
        email = data.get("email")
        userID = data.get("userID")
        check_form = select_all_from_userid(userID)
        # password = current_user.get("password")
        if not (data and check_form and email and userID):
            return jsonify({"message": "Unauthorized user token is invalid!!!"}), 403
        return func(formID=formID, userID=userID)

    return decorator
