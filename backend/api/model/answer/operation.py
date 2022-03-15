from MySQLdb import OperationalError, IntegrityError
from api.model.mysqlmanager import MySQLManager
from api.model.answer.model import (
    select_all_answer_table,
    insert_into_answer_table,
    delete_answer_from_id,
    select_answer_from_userid,
    update_answer_table
)


def get_answers():
    with MySQLManager() as sql:
        conn = sql
        cur = conn.cursor()
        if select_all_answer_table(cur) > 0:
            results = cur.fetchall()
            userID = results[0][-1]
            datas = []
            for result in results:
                userID = result[-1]
                result = result[:-1]
                datas.append(
                    dict(
                        zip(
                            (
                                "id",
                                "created_at",
                                "blockID",
                                "answer",
                            ),
                            result,
                        )
                    )
                )

            # datas.append({"userID": userID})
            return {"userID": userID, "answers": datas}


def set_answer(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        return insert_into_answer_table(conn, cur, **kwargs)


def delete_answer_by_id(answerID):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        return delete_answer_from_id(conn, cur, answerID)


def get_user_answer(userID):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        if select_answer_from_userid(cur, userID):
            results = cur.fetchall()
            return results


def update_answer_details(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()

        return update_answer_table(conn, cur, **kwargs)
