from os import environ
from api.model.mysqlmanager import MySQLManager
from api.model.user.model import (
    create_user_table,
    insert_into_user_table,
    select_all_user_table,
)

hostname = environ.get("MYSQL_HOST")
username = environ.get("MYSQL_USER")
password = environ.get("MYSQL_PASSWORD")
database = environ.get("MYSQL_DB")


def get_all_user():
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        if select_all_user_table(cur) > 0:
            results = cur.fetchall()
            datas = []
            for result in results:
                datas.append(
                    dict(
                        zip(
                            (
                                "id",
                                "created_at",
                                "name",
                                "address",
                                "phone",
                                "email",
                                "password",
                            ),
                            result,
                        )
                    )
                )
            return datas


def set_user(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        name = kwargs.get("name")
        address = kwargs.get("address")
        phone = kwargs.get("phone")
        email = kwargs.get("email")
        passwd = kwargs.get("password")

        return insert_into_user_table(
            conn,
            cur,
            name=name,
            address=address,
            phone=phone,
            email=email,
            password=passwd,
        )
