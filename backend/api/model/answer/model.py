from MySQLdb import OperationalError, IntegrityError
from .query import (
    CREATE_ANSWER_TABLE,
    SELECT_ALL_ANSWER_TABLE,
    INSERT_INTO_ANSWER_TABLE,
    DROP_ANSWER_TABLE,
    SELECT_ANSWER_WHERE_USERID_AND_BLOCKID,
    DELETE_ANSWER_FROM_ID,
    SELECT_ANSWER_FROM_USERID,
    UPDATE_ANSWER_TABLE,
)


def create_answer_table(conn, cur):
    try:
        cur.execute(CREATE_ANSWER_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def drop_answer_table(conn, cur):
    try:
        cur.execute(DROP_ANSWER_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def select_all_answer_table(cur):
    try:
        return cur.execute(SELECT_ALL_ANSWER_TABLE)
    except OperationalError:
        return False
    else:
        return True


def select_answer_where_userid_and_blockid(cur, userID, blockID):
    try:
        return cur.execute(SELECT_ANSWER_WHERE_USERID_AND_BLOCKID, (userID, blockID))
    except OperationalError:
        return False
    else:
        return True


def insert_into_answer_table(conn, cur, **kwargs):
    try:
        answerID = kwargs.get("answerID")
        blockID = kwargs.get("blockID")
        userID = kwargs.get("userID")
        answer = kwargs.get("answer")
        if select_answer_where_userid_and_blockid(cur, userID, blockID):
            return False
        cur.execute(INSERT_INTO_ANSWER_TABLE, (answerID, blockID, userID, answer))
        conn.commit()
    except IntegrityError or OperationalError:
        return False
    else:
        return True


def delete_answer_from_id(conn, cur, answerID):
    try:
        cur.execute(DELETE_ANSWER_FROM_ID, (answerID,))
        conn.commit()
    except IntegrityError or OperationalError:
        return False
    else:
        return True


def select_answer_from_userid(cur, userID):
    try:
        cur.execute(SELECT_ANSWER_FROM_USERID, (userID,))
    except IntegrityError or OperationalError:
        return False
    else:
        return True


def update_answer_table(conn, cur, **kwargs):
    try:
        answerID = kwargs.get("answerID")
        answer = kwargs.get("answer")
        cur.execute(
            UPDATE_ANSWER_TABLE,
            (answer, answerID),
        )
        conn.commit()
    except IntegrityError:
        return False
    else:
        return True
