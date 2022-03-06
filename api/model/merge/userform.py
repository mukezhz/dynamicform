from os import environ
from MySQLdb import OperationalError, IntegrityError
from api.model.mysqlmanager import MySQLManager


hostname = environ.get("MYSQL_HOST")
username = environ.get("MYSQL_USER")
password = environ.get("MYSQL_PASSWORD")
database = environ.get("MYSQL_DB")


CREATE_USER_FORM_TABLE = """
CREATE TABLE UserForm (
    id int unsigned not null auto_increment primary key,
    created_at timestamp not null default CURRENT_TIMESTAMP,
    userID VARCHAR(36) not null, 
    formID VARCHAR(36) not null unique,
    CONSTRAINT Cons_User FOREIGN KEY FK_USER (userID) REFERENCES User(id),
    CONSTRAINT Cons_Form FOREIGN KEY FK_FORM (formID) REFERENCES Form(id)
);
"""

DROP_USER_FORM_TABLE = """
    DROP TABLE UserForm;
"""

INSERT_INTO_USER_FORM = """
    INSERT INTO UserForm (userID, formID)
    VALUES (%s, %s);
"""


def create_user_form_table(conn, cur):
    try:
        cur.execute(CREATE_USER_FORM_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def drop_user_form_table(conn, cur):
    try:
        cur.execute(DROP_USER_FORM_TABLE)
        conn.commit()
    except OperationalError:
        return False
    else:
        return True


def initiate_user_form(userID=None, formID=None):
    with MySQLManager(hostname, username, password, database) as sql:
        conn = sql
        cur = conn.cursor()
        try:
            cur.execute(INSERT_INTO_USER_FORM, (userID, formID))
            conn.commit()
        except OperationalError:
            return False
        else:
            return True
