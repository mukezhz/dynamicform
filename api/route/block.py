from flask import Blueprint
from api.controller.block import index

block_api = Blueprint("block_api", __name__)

block_api.route("/", methods=["GET"])(index)