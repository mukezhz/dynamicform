from uuid import uuid4
import json
from flask import request, jsonify
from api.model.answer.operation import get_answers, set_answer


def index():
    if request.method == "GET":
        datas = get_answers()
        # return the list of users after fetching the users from database
        return jsonify(datas), 200
    else:
        return jsonify({"message": "Method Not Implemented"}), 405


def create_answer():
    message = ""
    if request.method == "POST":
        datas = json.loads(request.data)
        title = datas.get("title")
        userID = datas.get("userID")
        formID = datas.get("formID")
        blocks = datas.get("blocks")
        for block in blocks:
            answerID = uuid4()
            answer = block.get("answer")
            blockID = block.get("blockID")
            if not set_answer(
                answerID=answerID, blockID=blockID, userID=userID, answer=answer
            ):
                message = "Error has been occurred while setting answer"
                return jsonify({"message": message}), 400
        else:
            message = "Answer is set"
        return jsonify({"message": message}), 200
