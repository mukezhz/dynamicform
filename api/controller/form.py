from uuid import uuid4
import json
from flask import request, jsonify
from api.model.form.operation import get_forms, set_form
from api.model.block.operation import set_block
from api.model.merge.userform import initiate_user_form
from api.model.merge.formblock import initiate_form_block


def index():
    if request.method == "GET":
        datas = get_forms()
        # return the list of users after fetching the users from database
        return jsonify(datas), 200
    else:
        return jsonify({"message": "Method Not Implemented"}), 405


def create_form():
    if request.method == "POST":
        datas = json.loads(request.data)
        userID = datas.get("userID")
        title = datas.get("title")
        subtitle = datas.get("subtitle")
        blocks = datas.get("blocks")
        formID = uuid4()
        message = ""
        if set_form(id=formID, title=title, subtitle=subtitle):
            if initiate_user_form(userID=userID, formID=formID):
                for block in blocks:
                    blockID = uuid4()
                    question = block.get("question")
                    typeof = block.get("typeof")
                    isRequired = block.get("isRequired")
                    options = block.get("options")
                    answer = block.get("answer")
                    if set_block(
                        id=blockID,
                        typeof=typeof,
                        isRequired=isRequired,
                        answer=answer,
                        options=options,
                        question=question,
                    ):
                        if initiate_form_block(formID=formID, blockID=blockID):
                            message = "Successfully Form is filled"
                        else:
                            message = "Error while filling Form"
        return jsonify({"message": message}), 201
