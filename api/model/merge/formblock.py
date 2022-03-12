from os import environ
from api.model.mysqlmanager import MySQLManager
from MySQLdb import OperationalError, IntegrityError

hostname = environ.get("MYSQL_HOST")
username = environ.get("MYSQL_USER")
password = environ.get("MYSQL_PASSWORD")
database = environ.get("MYSQL_DB")


CREATE_FORM_BLOCK_TABLE = """
    CREATE TABLE FormBlock (
        id int unsigned not null auto_increment primary key,
        created_at timestamp not null default CURRENT_TIMESTAMP,
        formID VARCHAR(36) not null,
        blockID VARCHAR(36) not null,
        CONSTRAINT Cons_Form_Block FOREIGN KEY FK_FORM (formID) REFERENCES Form(id),
        CONSTRAINT Cons_Block FOREIGN KEY FK_USER (blockID) REFERENCES Block(id)
    );
"""

DROP_FORM_BLOCK_TABLE = """
    DROP TABLE FormBlock;
"""

INSERT_INTO_FORM_BLOCK = """
    INSERT INTO FormBlock (formID, blockID)
    VALUES (%s, %s);
"""

INNER_JOIN_FORM_BLOCK = """
    SELECT Form.id, Form.title, Form.subtitle, Block.id, Block.typeof, Block.isRequired, Block.options, Block.question
    FROM Form
    INNER JOIN FormBlock 
    ON Form.id=FormBlock.formID
    INNER JOIN Block
    ON FormBlock.blockID=Block.id
    WHERE Form.id=%s
"""

INNER_JOIN_FORM_BLOCK_ANSWER = """
    SELECT Form.id, Form.title, Form.subtitle, Block.id, Block.typeof, Block.isRequired, Block.options, Block.question, Answer.id, Answer.answer
    FROM Form
    INNER JOIN FormBlock 
    ON Form.id=FormBlock.formID
    INNER JOIN Block
    ON FormBlock.blockID=Block.id
    INNER JOIN Answer
    ON Answer.blockID=Block.id
    WHERE Form.id=%s
"""

DELETE_FORM_BLOCK_FIELD = """
    DELETE FROM FormBlock WHERE formID=%s
"""


SELECT_BLOCKID_FROM_FORMID = """
    SELECT blockID FROM FormBlock WHERE formID=%s
"""


def create_form_block_table(conn, cur):
    try:
        cur.execute(CREATE_FORM_BLOCK_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def drop_form_block_table(conn, cur):
    try:
        cur.execute(DROP_FORM_BLOCK_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def initiate_form_block(formID=None, blockID=None):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        try:
            cur.execute(INSERT_INTO_FORM_BLOCK, (formID, blockID))
            conn.commit()
        except OperationalError:
            return False
        else:
            return True


def inner_join_form_block(cur, formID=None):
    try:
        cur.execute(INNER_JOIN_FORM_BLOCK, (formID,))
    except OperationalError:
        return False
    else:
        return True


def inner_join_form_block_answer(cur, formID=None):
    try:
        cur.execute(INNER_JOIN_FORM_BLOCK_ANSWER, (formID,))
    except OperationalError:
        return False
    else:
        return True


def get_form_block(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        formID = kwargs.get("formID")
        if inner_join_form_block(cur, formID=formID) > 0:
            results = cur.fetchall()
            formID = results[0][0]
            title = results[0][1]
            subtite = results[0][2]
            datas = []
            for result in results:
                result = result[3:]
                datas.append(
                    dict(
                        zip(
                            (
                                "blockID",
                                "typeof",
                                "isRequired",
                                "options",
                                "question",
                            ),
                            result,
                        )
                    )
                )

            return {
                "blocks": datas,
                "formID": formID,
                "title": title,
                "subtite": subtite,
            }


def get_form_block_with_answer(**kwargs):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        formID = kwargs.get("formID")
        if inner_join_form_block_answer(cur, formID=formID) > 0:
            results = cur.fetchall()
            datas = []
            for result in results:
                datas.append(
                    dict(
                        zip(
                            (
                                "formID",
                                "title",
                                "subtitle",
                                "blockID",
                                "typeof",
                                "isRequired",
                                "options",
                                "question",
                                "answerID",
                                "answer",
                            ),
                            result,
                        )
                    )
                )
            return datas


def delete_form_block_field(formID):
    with MySQLManager(hostname, username, password, database) as conn:
        cur = conn.cursor()
        try:
            cur.execute(DELETE_FORM_BLOCK_FIELD, (formID,))
            conn.commit()
        except OperationalError:
            return False
        else:
            return True


def select_blockid_from_formid(formID):
    with MySQLManager(hostname, username, password, database) as conn:
        cur = conn.cursor()
        try:
            cur.execute(SELECT_BLOCKID_FROM_FORMID, (formID,))
            resp = cur.fetchall()
        except OperationalError:
            return False
        else:
            return resp