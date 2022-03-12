from uuid import uuid4
import json
from flask import request, jsonify
from api.model.answer.operation import (
    get_answers,
    set_answer,
    get_user_answer,
    delete_answer_by_id,
    update_answer_details
)


def index():
    if request.method == "GET":
        datas = get_answers()
        if not datas:
            return jsonify({"message": "No any answers available!!!"}), 200
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
            message = "Answer has been set!!!"
        return jsonify({"message": message}), 200


def get_answer_of_user():
    if request.method == "GET":
        userID = request.args.get("userID")
        datas = get_user_answer(userID)
        answerIDs = [data[0] for data in datas]
        return answerIDs


def delete_answer(answerID):
    if request.method == "DELETE" and delete_answer_by_id(answerID=answerID):
        return jsonify({"message": "Answer deleted successfully!!!"}), 200
    else:
        return jsonify({"message": "Invalid id has been provided!!!"}), 400


def update_answer(answerID):
    if request.method == "PUT":
        datas = request.json
        answer = datas.get("answer")
        answerID = datas.get("answerID")
        # TODO: checking need to be done before data storage
        if update_answer_details(
            answerID=answerID,
            answer=answer,
        ):
            return (
                jsonify({"message": "Answer has been successfully updated!!!"}),
                200,
            )
            # 201: Success
        else:
            return (
                jsonify({"message": "Error while value updation!!!"}),
                400,
            )
            # 400: Bad Request
