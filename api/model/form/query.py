CREATE_FORM_TABLE = """
CREATE TABLE Form (
  id int unsigned not null auto_increment primary key,
  created_at timestamp not null default CURRENT_TIMESTAMP,
  title VARCHAR(100) not null,
  subtitle varchar(255) null
);
"""

DROP_FORM_TABLE = """
  DROP TABLE Form;
"""

INSERT_INTO_FORM_TABLE = """
  INSERT INTO Form (title, subtitle)
  VALUES (%s , %s);
"""

SELECT_ALL_FORM_TABLE = """
  SELECT * FROM Form;
"""

DELETE_FORM_FROM_ID = """
  DELETE FROM Form WHERE id=%s;
"""