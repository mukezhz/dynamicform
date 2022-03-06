from os import environ
from MySQLdb import OperationalError, IntegrityError
from api.model.mysqlmanager import MySQLManager
from api.model.block.model import select_all_block_table, insert_into_block_table

hostname = environ.get("MYSQL_HOST")
username = environ.get("MYSQL_USER")
password = environ.get("MYSQL_PASSWORD")
database = environ.get("MYSQL_DB")


def get_blocks():
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        if select_all_block_table(cur) > 0:
            results = cur.fetchall()
            datas = []
            for result in results:
                datas.append(
                    dict(
                        zip(
                            (
                                "id",
                                "created_at",
                                "isRequired",
                                "answer",
                                "options",
                                "question",
                            ),
                            result,
                        )
                    )
                )
            return datas


def set_block(**kwargs):
    id = kwargs.get("id")
    typeof = kwargs.get("typeof")
    isRequired = kwargs.get("isRequired")
    answer = kwargs.get("answer")
    options = kwargs.get("options")
    question = kwargs.get("question")
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        return insert_into_block_table(
            conn,
            cur,
            id=id,
            typeof=typeof,
            isRequired=isRequired,
            answer=answer,
            options=options,
            question=question,
        )
