from flask import Blueprint
from api.controller.answer import index, create_answer

answer_api = Blueprint("answer_api", __name__)

answer_api.route("/", methods=["GET"])(index)
answer_api.route("/create", methods=["POST"])(create_answer)