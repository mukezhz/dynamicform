from MySQLdb import OperationalError, IntegrityError
from .query import (
    CREATE_BLOCK_TABLE,
    SELECT_ALL_BLOCK_TABLE,
    INSERT_INTO_BLOCK_TABLE,
    DROP_BLOCK_TABLE,
    UPDATE_BLOCK_TABLE,
    DELETE_BLOCK_FROM_ID,
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
        blockID = kwargs.get("blockID")
        typeof = kwargs.get("typeof")
        isRequired = kwargs.get("isRequired")
        options = kwargs.get("options")
        question = kwargs.get("question")
        cur.execute(
            INSERT_INTO_BLOCK_TABLE,
            (blockID, typeof, isRequired, options, question),
        )
        conn.commit()
    except IntegrityError and OperationalError:
        return False
    else:
        return True


def update_block_table(conn, cur, **kwargs):
    try:
        blockID = kwargs.get("blockID")
        typeof = kwargs.get("typeof")
        isRequired = kwargs.get("isRequired")
        options = kwargs.get("options")
        question = kwargs.get("question")
        cur.execute(
            UPDATE_BLOCK_TABLE,
            (typeof, isRequired, options, question, blockID),
        )
        conn.commit()
    except IntegrityError:
        return False
    else:
        return True


def delete_block_from_id(conn, cur, blockID):
    try:
        if not cur.execute(DELETE_BLOCK_FROM_ID, (blockID,)):
            return False
        conn.commit()
    except OperationalError:
        return False
    else:
        return True
