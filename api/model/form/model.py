from uuid import uuid4
from MySQLdb import OperationalError, IntegrityError
from .query import (
    CREATE_FORM_TABLE,
    SELECT_ALL_FORM_TABLE,
    INSERT_INTO_FORM_TABLE,
    DROP_FORM_TABLE,
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
        id = kwargs.get("id")
        title = kwargs.get("title")
        subtitle = kwargs.get("subtitle")
        cur.execute(INSERT_INTO_FORM_TABLE, (id, title, subtitle))
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
