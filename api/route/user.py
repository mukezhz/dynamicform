from flask import Blueprint
from api.controller.user import index, create_user

user_api = Blueprint("user_api", __name__)

user_api.route("/", methods=["GET", "POST"])(index)
user_api.route("/create", methods=["POST"])(create_user)