from pymongo import MongoClient


class DB:
    def __init__(self, connstr='mongodb://localhost:27017') -> None:
        try:
            self.client = MongoClient(connstr)
            self.python_course_db = self.client.get_database('python_course')

        except:
            print('Can not connect to server!')


    def list_collections(self, db_name):
         db = self.client[db_name]
         print( db.list_collection_names() )


    def insert_user(self, name, passwd):
        # db_name='python_course'
        # collection = 'users'

        try:
            res = self.python_course_db.users.insert_one({
                'name':name,
                'password':passwd
            })

            return res
        except Exception as e:
            raise( e )

    def get_user_by_name(self, name):
        user = self.python_course_db.users.find_one()