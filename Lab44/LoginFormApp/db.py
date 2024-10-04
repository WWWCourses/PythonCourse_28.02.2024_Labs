import mysql.connector

# from mysql.connector import connection


def make_connection(user, password, db, host="localhost", port=3306):
    cnx = None
    try:
        cnx = mysql.connector.connect(
            user=user, password=password, db=db, host=host, port=port
        )

    except mysql.connector.Error as e:
        print(e)

    print("*** Connection Established ***")
    return cnx


def authenticate(cnx, user_name, password):
    # create a cursor for the connection
    cur = cnx.cursor()

    # prepare SQL query:
    q = f"""
		SELECT * FROM users
			WHERE username='{user_name}'
			AND `password`='{password}'
	"""
    # execute the query
    cur.execute(q)

    # we are only interested if 1 or 0 rows are returned
    res = cur.fetchone()

    # do something with the result
    if res:
        print("Authentication Successful")
    else:
        print("Authentication Failed")

