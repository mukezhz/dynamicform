CREATE_USER_TABLE = """
CREATE TABLE User (
  id varchar(36) NOT NULL,
  created_at timestamp NOT NULL DEFAULT current_timestamp(),
  name varchar(150) NOT NULL,
  address varchar(100) NOT NULL,
  phone varchar(15) DEFAULT NULL,
  email varchar(100) NOT NULL UNIQUE,
  password varchar(100) NOT NULL,
  token varchar(500) DEFAULT NULL,
  PRIMARY KEY (id)
);
"""

INSERT_INTO_USER_TABLE = """
  INSERT INTO User (id, name, address, phone, email, password)
  VALUES (%s , %s, %s, %s, %s, %s);
"""

SELECT_ALL_USER_TABLE = """
  SELECT id, name, address, phone, email FROM User ;
"""

DROP_USER_TABLE = """
  DROP TABLE User;
"""

GET_USER_FROM_ID = """
  SELECT id, created_at, name, email, address, phone FROM User WHERE id=%s;
"""

DELETE_USER_FROM_ID = """
  DELETE FROM User WHERE id=%s;
"""


UPDATE_USER_TABLE = """
  UPDATE User SET name=%s, address=%s, phone=%s, email=%s
  WHERE id=%s;
"""

SELECT_PASSWORD_TOKEN_FROM_EMAIL = """
  SELECT id, password, token FROM User WHERE email=%s;
"""

SELECT_ALL_FROM_TOKEN = """
  SELECT * FROM User WHERE token=%s;
"""

UPDATE_TOKEN = """
  UPDATE User SET token=%s
  WHERE email=%s;
"""
