from flask import Blueprint
from api.controller.form import index, create_form

form_api = Blueprint("form_api", __name__)

form_api.route("/", methods=["GET"])(index)
form_api.route("/create", methods=["POST"])(create_form)