from flask import Blueprint
from api.controller.form import (
    index,
    create_form,
    get_form,
    get_form_with_answer,
    update_form,
    delete_form,
)

form_api = Blueprint("form_api", __name__)

form_api.route("/", methods=["GET"])(index)
form_api.route("/<formID>", methods=["GET"])(get_form)
form_api.route("/answer/<formID>", methods=["GET"])(get_form_with_answer)
form_api.route("/", methods=["POST"])(create_form)
form_api.route("/", methods=["PUT"])(update_form)
form_api.route("/<formID>", methods=["PUT"])(update_form)
form_api.route("/<formID>", methods=["DELETE"])(delete_form)
