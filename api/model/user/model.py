from uuid import uuid4
from MySQLdb import OperationalError, IntegrityError
from werkzeug.security import generate_password_hash
from .query import CREATE_USER_TABLE, INSERT_INTO_USER_TABLE, SELECT_ALL_UESR_TABLE


def create_user_table(cur):
    try:
        cur.execute(CREATE_USER_TABLE)
    except OperationalError:
        return False
    else:
        return True


def insert_into_user_table(conn, cur, **kwargs):
    try:
        id = uuid4()
        name = kwargs.get("name")
        address = kwargs.get("address")
        phone = kwargs.get("phone")
        email = kwargs.get("email")
        password = kwargs.get("password")
        hashed_password = generate_password_hash(password)
        cur.execute(
            INSERT_INTO_USER_TABLE, (id, name, address, phone, email, hashed_password)
        )
        conn.commit()
    except IntegrityError:
        return False
    else:
        return True


def select_all_user_table(cur):
    try:
        return cur.execute(SELECT_ALL_UESR_TABLE)
    except OperationalError:
        return False
    else:
        return True
