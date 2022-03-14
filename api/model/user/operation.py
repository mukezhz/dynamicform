from os import environ
from api.model.mysqlmanager import MySQLManager
from api.model.user.model import (
    create_user_table,
    insert_into_user_table,
    select_all_user_table,
    get_user_from_id,
    delete_user_from_id,
    update_user_table,
    select_password_from_email,
    update_token,
    select_all_from_token,
)

hostname = environ.get("MYSQL_HOST")
username = environ.get("MYSQL_USER")
password = environ.get("MYSQL_PASSWORD")
database = environ.get("MYSQL_DB")


def get_users():
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
                                "name",
                                "address",
                                "phone",
                                "email",
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
        userID = kwargs.get("userID")
        name = kwargs.get("name")
        address = kwargs.get("address")
        phone = kwargs.get("phone")
        email = kwargs.get("email")
        passwd = kwargs.get("password")

        return insert_into_user_table(
            conn,
            cur,
            userID=userID,
            name=name,
            address=address,
            phone=phone,
            email=email,
            password=passwd,
        )


def get_user_details(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        userID = kwargs.get("userID")
        if get_user_from_id(cur, userID) > 0:
            result = cur.fetchone()
            return dict(
                zip(
                    (
                        "id",
                        "created_at",
                        "name",
                        "email",
                        "address",
                        "phone",
                    ),
                    result,
                )
            )


def delete_user_details(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        userID = kwargs.get("userID")
        return delete_user_from_id(conn, cur, userID)


def update_user_details(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        userID = kwargs.get("userID")
        name = kwargs.get("name")
        address = kwargs.get("address")
        phone = kwargs.get("phone")
        email = kwargs.get("email")

        return update_user_table(
            conn,
            cur,
            userID=userID,
            name=name,
            address=address,
            phone=phone,
            email=email,
        )


def select_user_password_token_using_email(email):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        if select_password_from_email(cur, email) > 0:
            results = cur.fetchone()
            return {"id": results[0], "password": results[1], "token": results[-1]}
        return None


def update_user_token(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()

        return update_token(conn, cur, **kwargs)


def get_all_from_token(token):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        if select_all_from_token(cur, token) > 0:
            result = cur.fetchone()
            return dict(
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
            # return {"id": results[0], "password": results[1], "token": results[-1]}
        return None
