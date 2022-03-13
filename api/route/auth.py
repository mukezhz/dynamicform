from flask import Blueprint
from api.controller.auth import (
    login,
    logout,
    register,
    token,
)

auth_api = Blueprint("auth_api", __name__)

auth_api.route("/login", methods=["POST", "GET"])(login)
auth_api.route("/register", methods=["POST"])(register)
auth_api.route("/logout", methods=["POST"])(logout)
auth_api.route("/token", methods=["POST"])(
    token
)  # to generate new access token from refresh token
