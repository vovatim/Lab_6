from mysql import connector as MySQLdb

class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host = self.host,
                user = self.user,
                passwd = self.password,
                db = self.db,
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()

class User:
    def __init__(self, db_connection, name, age):
        self.db_connection = db_connection.connection
        self.name = name
        self.age = age

    def save(self):
        u = self.db_connection.cursor()
        u.execute("INSERT INTO users (`name`, age) VALUES (%s, %s)", (self.name, self.age,))
        self.db_connection.commit()
        u.close()


con = Connection('newuser', '123', 'new_schema')

with con:
    u = User(con, 'Pet', 22)
    u.save()
