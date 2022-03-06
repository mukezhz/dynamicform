from MySQLdb import OperationalError, IntegrityError
from .query import (
    CREATE_BLOCK_TABLE,
    SELECT_ALL_BLOCK_TABLE,
    INSERT_INTO_BLOCK_TABLE,
    DROP_BLOCK_TABLE,
)


def create_block_table(conn, cur):
    try:
        cur.execute(CREATE_BLOCK_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def drop_block_table(conn, cur):
    try:
        cur.execute(DROP_BLOCK_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def select_all_block_table(cur):
    try:
        return cur.execute(SELECT_ALL_BLOCK_TABLE)
    except OperationalError:
        return False
    else:
        return True


def insert_into_block_table(conn, cur, **kwargs):
    try:
        id = kwargs.get("id")
        typeof = kwargs.get("typeof")
        isRequired = kwargs.get("isRequired")
        answer = kwargs.get("answer")
        options = kwargs.get("options")
        question = kwargs.get("question")
        cur.execute(
            INSERT_INTO_BLOCK_TABLE, (id, typeof, isRequired, answer, options, question)
        )
        conn.commit()
    except IntegrityError:
        return False
    else:
        return True
