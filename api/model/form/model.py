from MySQLdb import OperationalError, IntegrityError
from .query import (
    CREATE_FORM_TABLE,
    SELECT_ALL_FORM_TABLE,
    INSERT_INTO_FORM_TABLE,
    DROP_FROM_TABLE,
)


def create_form_table(cur):
    try:
        cur.execute(CREATE_FORM_TABLE)
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
        name = kwargs.get("title")
        address = kwargs.get("subtitle")
        cur.execute(INSERT_INTO_FORM_TABLE, (title, subtitle))
        conn.commit()
    except IntegrityError:
        return False
    else:
        return True


def drop_form_table(cur):
    try:
        cur.execute(DROP_FROM_TABLE)
    except OperationalError:
        return False
    else:
        return True
