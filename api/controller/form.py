from flask import request, jsonify
from api.model.form.operation import get_forms


def index():
    if request.method == "GET":
        datas = get_forms()
        # return the list of users after fetching the users from database
        return jsonify(datas), 200
    else:
        return jsonify({"message": "Method Not Implementd"}), 405
