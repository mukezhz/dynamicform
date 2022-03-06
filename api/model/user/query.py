CREATE_USER_TABLE = """
CREATE TABLE User (
  id varchar(36) NOT NULL,
  created_at timestamp NOT NULL DEFAULT current_timestamp(),
  name varchar(255) NOT NULL,
  address varchar(255) NOT NULL,
  phone varchar(255) DEFAULT NULL,
  email varchar(255) NOT NULL UNIQUE,
  password varchar(255) NOT NULL,
  PRIMARY KEY (id)
);
"""

INSERT_INTO_USER_TABLE = """
  INSERT INTO User (id, name, address, phone, email, password)
  VALUES (%s , %s, %s, %s, %s, %s);
"""

SELECT_ALL_USER_TABLE = """
  SELECT * FROM User ;
"""

DROP_USER_TABLE = """
  DROP TABLE User;
"""

GET_USER_FROM_ID = """
  SELECT * FROM User WHERE id=%s;
"""

DELETE_USER_FROM_ID = """
  DELETE FROM User WHERE id=%s;
"""
