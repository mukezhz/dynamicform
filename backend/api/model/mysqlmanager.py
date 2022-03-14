import MySQLdb as mysql


class MySQLManager:
    def __init__(self, hostname, username, password, database, *args, **kwargs):
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
