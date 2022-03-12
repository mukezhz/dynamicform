from flask import Blueprint
from api.controller.answer import (
    index,
    create_answer,
    get_answer_of_user,
    delete_answer,
    update_answer
)

answer_api = Blueprint("answer_api", __name__)

answer_api.route("/", methods=["GET"])(index)
answer_api.route("/user", methods=["GET"])(get_answer_of_user)
answer_api.route("/", methods=["POST"])(create_answer)
answer_api.route("/<answerID>", methods=["DELETE"])(delete_answer)
answer_api.route("/<answerID>", methods=["PUT"])(update_answer)
