from MySQLdb import OperationalError, IntegrityError
from api.model.mysqlmanager import MySQLManager
from api.model.block.model import (
    select_all_block_table,
    insert_into_block_table,
    update_block_table,
    delete_block_from_id
)


def get_blocks():
    with MySQLManager() as sql:
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
                                "typeof",
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
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        return insert_into_block_table(conn, cur, **kwargs)


def update_block_details(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        return update_block_table(conn, cur, **kwargs)


def delete_block_details(blockID):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        return delete_block_from_id(conn, cur, blockID)