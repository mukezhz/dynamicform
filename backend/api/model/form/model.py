from uuid import uuid4
from MySQLdb import OperationalError, IntegrityError
from .query import (
    CREATE_FORM_TABLE,
    SELECT_ALL_FORM_TABLE,
    INSERT_INTO_FORM_TABLE,
    DROP_FORM_TABLE,
    GET_FORM_FROM_ID,
    DELETE_FORM_FROM_ID,
    UPDATE_FORM_TABLE,
)


def create_form_table(conn, cur):
    try:
        cur.execute(CREATE_FORM_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def drop_form_table(conn, cur):
    try:
        cur.execute(DROP_FORM_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def select_all_form_table(cur):
    try:
        return cur.execute(SELECT_ALL_FORM_TABLE)
    except OperationalError:
        return False
    else:
        return True


def insert_into_form_table(conn, cur, **kwargs):
    try:
        formID = kwargs.get("formID")
        title = kwargs.get("title")
        subtitle = kwargs.get("subtitle")
        cur.execute(INSERT_INTO_FORM_TABLE, (formID, title, subtitle))
        conn.commit()
    except IntegrityError:
        return False
    else:
        return True


def insert_dummy_data_into_form_table(cur):
    try:
        cur.execute(INSERT_INTO_FORM_TABLE, ("Untitled Title", ""))
    except IndentationError():
        return False
    else:
        return cur


def get_form_from_id(cur, formID):
    try:
        cur.execute(GET_FORM_FROM_ID, (formID,))
    except OperationalError:
        return False
    else:
        return True


def delete_form_from_id(conn, cur, formID):
    try:
        if not cur.execute(DELETE_FORM_FROM_ID, (formID,)):
            return False
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def update_form_table(conn, cur, **kwargs):
    try:
        formID = kwargs.get("formID")
        title = kwargs.get("title")
        subtitle = kwargs.get("subtitle")
        cur.execute(
            UPDATE_FORM_TABLE,
            (title, subtitle, formID),
        )
        conn.commit()
    except IntegrityError:
        return False
    else:
        return True
