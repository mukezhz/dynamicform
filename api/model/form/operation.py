from os import environ
from api.model.mysqlmanager import MySQLManager
from .model import select_all_form_table, insert_into_form_table, get_form_from_id


hostname = environ.get("MYSQL_HOST")
username = environ.get("MYSQL_USER")
password = environ.get("MYSQL_PASSWORD")
database = environ.get("MYSQL_DB")


def get_forms():
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        if select_all_form_table(cur) > 0:
            results = cur.fetchall()
            datas = []
            for result in results:
                datas.append(
                    dict(
                        zip(
                            (
                                "id",
                                "created_at",
                                "title",
                                "subtitle",
                            ),
                            result,
                        )
                    )
                )
            return datas


def set_form(**kwargs):
    id = kwargs.get("id")
    title = kwargs.get("title", "Untitled Title")
    subtitle = kwargs.get("subtitle", "")
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        return insert_into_form_table(conn, cur, id=id, title=title, subtitle=subtitle)


def get_form_details(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        formID = kwargs.get("formID")
        if get_form_from_id(cur, formID) > 0:
            results = cur.fetchall()
            result = results[0]
            return dict(
                zip(
                    (
                        "id",
                        "created_at",
                        "title",
                        "subtitle",
                    ),
                    result,
                )
            )
