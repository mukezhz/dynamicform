from uuid import uuid4
import json
from flask import request, jsonify
from api.model.form.operation import (
    get_forms,
    set_form,
    get_form_details,
    delete_form_details,
    update_form_details,
)
from api.model.block.operation import (
    set_block,
    update_block_details,
    delete_block_details,
)
from api.model.merge.userform import initiate_user_form, delete_user_form_field
from api.model.merge.formblock import (
    initiate_form_block,
    get_form_block,
    get_form_block_with_answer,
    delete_form_block_field,
    select_blockid_from_formid,
)
from api.utils.token import verify_user


def index():
    if request.method == "GET":
        datas = get_forms()
        # return the list of users after fetching the users from database
        return jsonify(datas), 200
    else:
        return jsonify({"message": "Method Not Implemented"}), 405


@verify_user
def create_form(**kwargs):
    check_userID = kwargs.get("userID")
    if not check_userID:
        return jsonify({"message": "Unauthorized user!!!"}), 403
    if request.method == "POST":
        datas = request.json
        title = datas.get("title")
        subtitle = datas.get("subtitle")
        userID = datas.get("userID")
        if not (check_userID == userID):
            return jsonify(({"message": "[Unauthorized user] user id didn't match!!!"}))
        blocks = datas.get("blocks")
        formID = uuid4()
        message = ""
        # Form is being created
        if set_form(formID=formID, title=title, subtitle=subtitle):
            # once form is create UserForm table is filled
            if initiate_user_form(userID=userID, formID=formID):
                for block in blocks:
                    blockID = uuid4()
                    question = block.get("question")
                    typeof = block.get("typeof")
                    isRequired = block.get("isRequired")
                    options = block.get("options")
                    # Block is being filled
                    if set_block(
                        blockID=blockID,
                        typeof=typeof,
                        isRequired=isRequired,
                        options=options,
                        question=question,
                    ):
                        if initiate_form_block(formID=formID, blockID=blockID):
                            message = "Successfully Form is filled"
                        else:
                            message = "Error while filling Form"
            else:
                delete_form_details(formID=formID)
                message = "Invalid User!!!"
        return jsonify({"message": message}), 201


@verify_user
def get_form(formID, **kwargs):
    if request.method == "GET":
        return jsonify(get_form_block(formID=formID)), 200
    else:
        return jsonify({"message": "Invalid id has been provided"}), 400


@verify_user
def get_form_with_answer(formID, **kwargs):
    if request.method == "GET":
        return jsonify(get_form_block_with_answer(formID=formID)), 200
    else:
        return jsonify({"message": "Invalid id has been provided"}), 400


@verify_user
def update_form(formID=None, **kwargs):
    if request.method == "PUT":
        datas = request.json
        title = datas.get("title")
        subtitle = datas.get("subtitle")
        blocks = datas.get("blocks")
        if not update_form_details(formID=formID, title=title, subtitle=subtitle):
            return jsonify({"message": "Invalid form id!!!"})
        for block in blocks:
            blockID = block.get("blockID")
            typeof = block.get("typeof")
            isRequired = block.get("isRequired")
            options = block.get("options")
            question = block.get("question")
            update_block_details(
                blockID=blockID,
                typeof=typeof,
                isRequired=isRequired,
                options=options,
                question=question,
            )
        return jsonify({"message": "Form update successful!!!"}), 200


@verify_user
def delete_form(formID, **kwargs):
    if request.method == "DELETE":
        blockIDs = select_blockid_from_formid(formID)
        try:
            if (
                delete_user_form_field(formID)
                and delete_form_block_field(formID)
                and delete_form_details(formID)
            ):
                for blockID in blockIDs:
                    if not delete_block_details(blockID):
                        return jsonify({"message": "Error while deleting block!!!"})
                return jsonify({"message": "Form deleted successfully!!!"}), 200
        except TypeError:
            pass
        return jsonify({"message": "Invalid id has been provided!!!"}), 400
