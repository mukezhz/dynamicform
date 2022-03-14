CREATE_FORM_TABLE = """
CREATE TABLE Form (
  id varchar(36) not null  primary key,
  created_at timestamp not null default CURRENT_TIMESTAMP,
  title VARCHAR(100) not null,
  subtitle varchar(255) null
);
"""

DROP_FORM_TABLE = """
  DROP TABLE Form;
"""

INSERT_INTO_FORM_TABLE = """
  INSERT INTO Form (id, title, subtitle)
  VALUES (%s, %s , %s);
"""

SELECT_ALL_FORM_TABLE = """
  SELECT * FROM Form;
"""

DELETE_FORM_FROM_ID = """
  DELETE FROM Form WHERE id=%s;
"""

GET_FORM_FROM_ID = """
  SELECT * FROM Form WHERE id=%s;
"""

UPDATE_FORM_TABLE = """
  UPDATE Form SET title=%s, subtitle=%s
  WHERE id=%s;
"""