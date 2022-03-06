from flask import Blueprint
from api.controller.form import index

form_api = Blueprint("form_api", __name__)

form_api.route("/", methods=["GET"])(index)
