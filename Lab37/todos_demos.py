import pymongo
from datetime import datetime

from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.python_course

# res = db.todos.insert_many([
# 	{
# 		"title": "Learn Python",
# 		"completed": True,
# 		"dueDate": datetime.fromisoformat("2021-07-01"),
# 		"priority": 1
# 	},
# 	{
# 		"title": "Learn Flask",
# 		"description":"Learn Flask to develop quick and easy web applications with the ability to scale up.",
# 		"completed": True,
# 		"dueDate": datetime.fromisoformat("2022-01-12"),
# 		"priority": 2
# 	},
# 	{
# 		"title": "Learn MongoDB",
# 		"completed": False,
# 		"dueDate": datetime.fromisoformat("2022-01-12"),
# 		"priority": 1
# 	},
# 	{
# 		"title": "Learn PyQT",
# 		"completed": False,
# 		"dueDate": datetime.fromisoformat("2021-12-01"),
# 		"priority": 2
# 	}
# ])

# print(res.inserted_ids)


# # get all
# todos = db.todos.find().sort('priority', pymongo.ASCENDING)
# pp.pprint(list(todos))

# get all todos, where 'dueDate'> 2021-12-01
# date_obj = datetime.fromisoformat("2021-12-01")
# new_todos = db.todos.find({"dueDate":{"$gt":date_obj}})
# pp.pprint(list(new_todos))

# -------------------------------- Projection -------------------------------- #
# # # get all
# todos = db.todos.find({},{'_id':0,'title':1 })
# for todo in todos:
#     print(todo['title'])


# # get all
# todos = db.todos.find().sort('priority', pymongo.ASCENDING)
# pp.pprint(list(todos))

# todos = db.todos.find(
#     {'title':{'$regex':r'python', '$options':'i'}}
# )
# pp.pprint(list(todos))

# ------------------------------- Create index ------------------------------- #
# db.todos.create_index([
#   ("title","text")
# ])

# db.todos.create_index([
#   ("title","text")
# ])

# todos = db.todos.find({ "$text": { "$search": "python" } })
# pp.pprint(list(todos))