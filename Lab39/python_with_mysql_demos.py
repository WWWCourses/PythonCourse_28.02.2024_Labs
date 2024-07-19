import mysql.connector
from mysql.connector import Error

db_config = {
    'user': 'test',
    'password': 'test1234',
    'host': '127.0.0.1',
    'database': 'testdb',
}

try:
    db = mysql.connector.connect(**db_config)

    if db.is_connected():
        print("Connected to MySQL database")
except Error as e:
    print(f"Error: '{e}'")




# insert many row
# users_data = [
#     ('Pesho2','pesho2@gmail.com'),
#     ('Pesho3','pesho3@gmail.com')
# ]

# with db.cursor() as cursor:
#     sql = f"""insert into users (name,email) values (%s,%s)"""
#     print(sql)
# # print(sql)
#     cursor.executemany(sql, users_data[0])
#     db.commit()


with db.cursor() as cursor:
    sql = 'SELECT * FROM users;'
    cursor.execute(sql)

    while True:
        row = cursor.fetchone()
        if row:
            print(row)
        else:
            break

