CREATE_BLOCK_TABLE = """
CREATE TABLE Block (
  id int unsigned not null auto_increment primary key,
  created_at timestamp not null default CURRENT_TIMESTAMP,
  typeof varchar(50) not null default "text",
  isRequired BOOLEAN null default 0,
  answer varchar(255) null,
  options varchar(455) null,
  question varchar(255) null
);
"""

DROP_BLOCK_TABLE = """
  DROP TABLE Block;
"""

INSERT_INTO_BLOCK_TABLE = """
  INSERT INTO Block (typeof, idRequired, answer, options, question)
  VALUES (%s , %s, %s, %s, %s);
"""

SELECT_ALL_BLOCK_TABLE = """
  SELECT * FROM Block ;
"""

DELETE_BLOCK_FROM_ID = """
  DELETE FROM Block WHERE id=%s;
"""
