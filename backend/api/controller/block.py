import json
from flask import request, jsonify
from api.model.block.operation import get_blocks


def index():
    if request.method == "GET":
        datas = get_blocks()
        # return the list of users after fetching the users from database
        return jsonify(datas), 200
    else:
        return jsonify({"message": "Method Not Implemented"}), 405
