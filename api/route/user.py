from flask import Blueprint
from api.controller.user import index, create_user, get_user, delete_user, update_user

user_api = Blueprint("user_api", __name__)

user_api.route("/", methods=["GET"])(index)
user_api.route("/<id>", methods=["GET"])(get_user)
user_api.route("/<id>", methods=["DELETE"])(delete_user)
user_api.route("/", methods=["POST"])(create_user)
user_api.route("/<id>", methods=["PUT"])(update_user)
