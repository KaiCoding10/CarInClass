import MySQLdb


class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.database
            )
            self.cursor = self.connection.cursor()
            if self.connection:
                print("Connected to MySQL server")
        except MySQLdb.Error as e:
            print(e)

    def close(self):
        self.cursor.close()
        self.connection.close
        print("Connection Closed")
