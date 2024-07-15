from pymongo import MongoClient
from bson.objectid import ObjectId

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

client = MongoClient('mongodb://localhost:27017')
db = client.get_database('python_course')

# # insert data
# res = db.users.insert_one(
#     {
#         "_id": 1,
#         "name": "John Doe",
#         "scores": [
#             {"subject": "Math", "score": 85},
#             {"subject": "English", "score": 90}
#         ]
#     }
# )


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


# # get all documents from collection
# documents = db.users.find()
# pp.pprint(list(documents))

# # Get all documents with key 'age'
# documents = db.users.find({'age':{'$exists':True}})
# pp.pprint(list(documents))

# # Get all documents where 'age'>=30:
# documents = db.users.find({'age':{'$gte':30}})
# pp.pprint(list(documents))

# Get all documents where 'age'>=30 and 'name' length>4
# # TODO: fix
# documents = db.users.find(
#     {
#         'and':[
#             {'age':{'$gte':30}},
#             {'name':{'$regex': r'.{2,}'}}
#         ]
#     }
# )
# pp.pprint(list(documents))


# documents = db.users.find(
#   {"scores.score": {"$gt": 80}},
#   {"scores.$": 1}
# )

# pp.pprint(list(documents))


# ---------------------------------- Update ---------------------------------- #
# res = db.users.update_one(
#     {'_id': ObjectId('669166674f8fa7560272049d')},
#     {'$set': {
#         'name':'ADA BYRON'
#     }}
# )
# pp.pprint(res)

# # get all documents from collection
# documents = db.users.find()
# pp.pprint(list(documents))


# ---------------------------------- Delete ---------------------------------- #
# Delete all documents, where 'password'=='12345678'
documents = db.users.delete_many({
    'password':'12345678'
})
pp.pprint(documents)






