from pymongo import MongoClient


# -------------------------- Connect to Mongo Server ------------------------- #

# client = MongoClient('mongodb://localhost:27017')
client = MongoClient()

# print( client.list_database_names() )

# List collections in a dbs:
db = client.python_course

# res = db.users.insert_one(
#     {
#         'name':'Ada',
#         'password':'12345678'
#     }
# )

# print(f'Doc id: {res.inserted_id}')

# print(alabala_db.list_collection_names())

# list all users
# all_users = db.users.find()
# for user in all_users:
#     print(user['name'])

# get user by name
users = db.users.find(
    {
        'name':'Ada',
    }, # filter
    {
        '_id':0,
        'password':1
    }
)
print(list(users))