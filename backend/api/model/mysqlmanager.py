from os import environ
import MySQLdb as mysql

hostname = environ.get("MYSQL_HOST")
username = environ.get("MYSQL_USER")
password = environ.get("MYSQL_PASSWORD")
database = environ.get("MYSQL_DATABASE")

class MySQLManager:
    def __init__(self, hostname=hostname, username=username, password=password, database=database, *args, **kwargs):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def __enter__(self):
        self.connection = mysql.connect(
            host=self.hostname,
            user=self.username,
            passwd=self.password,
            db=self.database,
        )
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()
