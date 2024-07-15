from pymongo import MongoClient
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)

client = MongoClient('mongodb://localhost:27017')
db = client.get_database('python_course')

# # insert data
# users_data = [
#     {
#         'name':'George',
#         'age':68
#     },
#     {
#         'name':'Johm',
#         'age': 30
#     }
# ]
# db.users.insert_many(users_data)


# get all documents from collection
# documents = db.users.find()
# pp.pprint(list(documents))

# # Get all documents with key 'age'
# documents = db.users.find({'age':{'$exists':True}})
# pp.pprint(list(documents))

# # Get all documents where 'age'>=30:
documents = db.users.find({'age':{'$gte':30}})
pp.pprint(list(documents))

# Get all documents where 'age'>=30 and 'name' length>4
# TODO: fix
documents = db.users.find(
    {
        'and':[
            {'age':{'$gte':30}},
            {'name':{'$regex': r'.{2,}'}}
        ]
    }
)
pp.pprint(list(documents))





