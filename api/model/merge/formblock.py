from MySQLdb import OperationalError, IntegrityError


CREATE_FORM_BLOCK_TABLE = """
CREATE TABLE FormBlock (
    id int unsigned not null auto_increment primary key,
    created_at timestamp not null default CURRENT_TIMESTAMP,
    formID int(10) unsigned NOT NULL,
    blockID int(10) unsigned NOT NULL,
    CONSTRAINT Cons_Form_Block FOREIGN KEY FK_FORM (formID) REFERENCES Form(id),
    CONSTRAINT Cons_Block FOREIGN KEY FK_USER (blockID) REFERENCES Block(id)
);
"""

DROP_FORM_BLOCK_TABLE = """
DROP TABLE FormBlock;
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
