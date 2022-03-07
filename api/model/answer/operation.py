from os import environ
from MySQLdb import OperationalError, IntegrityError
from api.model.mysqlmanager import MySQLManager
from api.model.answer.model import select_all_answer_table, insert_into_answer_table

hostname = environ.get("MYSQL_HOST")
username = environ.get("MYSQL_USER")
password = environ.get("MYSQL_PASSWORD")
database = environ.get("MYSQL_DB")


def get_answers():
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        if select_all_answer_table(cur) > 0:
            results = cur.fetchall()
            datas = []
            for result in results:
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
            return datas


def set_answer(**kwargs):
    answerID = kwargs.get("answerID")
    blockID = kwargs.get("blockID")
    userID = kwargs.get("userID")
    answer = kwargs.get("answer")
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        return insert_into_answer_table(
            conn,
            cur,
            answerID=answerID,
            blockID=blockID,
            userID=userID,
            answer=answer,
        )
