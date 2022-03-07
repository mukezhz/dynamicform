from flask import Blueprint
from api.controller.form import index, create_form, get_form, get_form_with_answer

form_api = Blueprint("form_api", __name__)

form_api.route("/", methods=["GET"])(index)
form_api.route("/<formID>", methods=["GET"])(get_form)
form_api.route("/answer/<formID>", methods=["GET"])(get_form_with_answer)
form_api.route("/create", methods=["POST"])(create_form)
