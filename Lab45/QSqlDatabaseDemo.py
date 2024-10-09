from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class DB:
    def __init__(self, user, password, db_name, host="localhost", port=3306):
        try:
            # Specify MySQL as the database type
            db = QSqlDatabase.addDatabase('QMYSQL')
            db.setHostName(host)
            db.setDatabaseName(db_name)
            db.setUserName(user)
            db.setPassword(password)

            if db.open():
                print("*** Connection Established ***")
            else:
                print(f"Database Error: {db.lastError().text()}")

        except Exception as e:
            print(f'Something went wrong!')



    def authenticate(self, user_name, password):
        query = QSqlQuery()


        q = """
            SELECT * FROM users
            WHERE username = :user_name
            AND password = :password
        """

        query.prepare(q)
        query.bindValue(":user_name" , user_name)
        query.bindValue(":password" , password)

        # Execute the query with provided parameters
        if query.exec():
            if query.next():
                return True
        else:
            print('No rows found')
            return False

if __name__ == "__main__":
    db = DB('test', 'test1234','pyqt_users_db')
    is_authenticated = db.authenticate(user_name='Mria', password='maria123')

    if is_authenticated:
        print('Authentication successful!')
    else:
        print('Authentication failed!')