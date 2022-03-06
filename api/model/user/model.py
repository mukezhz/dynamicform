from uuid import uuid4
from MySQLdb import OperationalError, IntegrityError
from werkzeug.security import generate_password_hash
from .query import (
    CREATE_USER_TABLE,
    INSERT_INTO_USER_TABLE,
    SELECT_ALL_USER_TABLE,
    DROP_USER_TABLE,
    GET_USER_FROM_ID,
    DELETE_USER_FROM_ID,
)


def create_user_table(conn, cur):
    try:
        cur.execute(CREATE_USER_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def drop_user_table(conn, cur):
    try:
        cur.execute(DROP_USER_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def delete_user_from_id(conn, cur, id):
    try:
        if not cur.execute(DELETE_USER_FROM_ID, (id,)):
            return False
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def insert_into_user_table(conn, cur, **kwargs):
    try:
        userID = kwargs.get("userID")
        name = kwargs.get("name")
        address = kwargs.get("address")
        phone = kwargs.get("phone")
        email = kwargs.get("email")
        password = kwargs.get("password")
        hashed_password = generate_password_hash(password)
        cur.execute(
            INSERT_INTO_USER_TABLE,
            (userID, name, address, phone, email, hashed_password),
        )
        conn.commit()
    except IntegrityError:
        return False
    else:
        return True


def select_all_user_table(cur):
    try:
        return cur.execute(SELECT_ALL_USER_TABLE)
    except OperationalError:
        return False
    else:
        return True


def get_user_from_id(cur, id):
    try:
        cur.execute(GET_USER_FROM_ID, (id,))
    except OperationalError:
        return False
    else:
        return True
