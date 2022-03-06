from MySQLdb import OperationalError, IntegrityError


CREATE_USER_FORM_TABLE = """
CREATE TABLE UserForm (
    id int unsigned not null auto_increment primary key,
    created_at timestamp not null default CURRENT_TIMESTAMP,
    userID VARCHAR(36) not null, 
    formID int(10) unsigned NOT NULL,
    CONSTRAINT Cons_User FOREIGN KEY FK_USER (userID) REFERENCES User(id),
    CONSTRAINT Cons_Form FOREIGN KEY FK_FORM (formID) REFERENCES Form(id)
);
"""

DROP_USER_FORM_TABLE = """
    DROP TABLE UserForm;
"""

def create_user_form_table(conn, cur):
    try:
        cur.execute(CREATE_USER_FORM_TABLE)
        conn.commit()
    except OperationalError:
        print("Errororor")
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
