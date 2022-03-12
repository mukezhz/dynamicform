CREATE_ANSWER_TABLE = """
  CREATE TABLE Answer (
    id VARCHAR(36) NOT NULL PRIMARY KEY,
    created_at timestamp NOT NULL default CURRENT_TIMESTAMP,
    blockID VARCHAR(36) NOT NULL,
    userID VARCHAR(36) NOT NULL,
    answer VARCHAR(255) NULL,
    CONSTRAINT Cons_Answer FOREIGN KEY FK_BLOCK (blockID) REFERENCES Block(id),
    CONSTRAINT Cons_AnswerUser FOREIGN KEY FK_USER (userID) REFERENCES User(id)
  );
"""

DROP_ANSWER_TABLE = """
  DROP TABLE Answer;
"""

INSERT_INTO_ANSWER_TABLE = """
  INSERT INTO Answer (id, blockID, userID, answer)
  VALUES (%s, %s, %s, %s);
"""

SELECT_ALL_ANSWER_TABLE = """
  SELECT * FROM Answer ;
"""

DELETE_ANSWER_FROM_ID = """
  DELETE FROM Answer WHERE userID=%s;
"""

SELECT_ANSWER_WHERE_USERID_AND_BLOCKID = """
  SELECT * FROM Answer WHERE userID=%s AND blockID=%s;
"""
