# services/user_service.py
from bson import ObjectId

from models.user import User
from utils.mongodb_util import MongoDBUtil


class UserService:
    def __init__(self):
        print('init')

    def create_user(self, mongo_uri, user_data):
        with MongoDBUtil.get_client(mongo_uri) as client:
            database = MongoDBUtil.get_database(client, 'users')
            user = user_data.to_dict()
            if '_id' in user and user['_id'] is not None:
                return MongoDBUtil.upsert_one(database, 'user_profiles', {'_id': user['_id']}, user)
            else:
                return MongoDBUtil.insert_one(database, 'user_profiles', user)

    def get_user_by_id(self, mongo_uri: str, user_id: str) -> User:
        with MongoDBUtil.get_client(mongo_uri) as client:
            database = MongoDBUtil.get_database(client, 'users')
            doc = MongoDBUtil.find_one(database, 'user_profiles', {'_id': ObjectId(user_id)})
            if doc:
                return User.from_dict(doc)
            return None


    def get_user(self, mongo_uri, username):
        with MongoDBUtil.get_client(mongo_uri) as client:
            database = MongoDBUtil.get_database(client, 'users')
            return MongoDBUtil.find_one(database, 'user_profiles', {'username': username})

    def update_user(self, mongo_uri, user_id, user_update_data):
        with MongoDBUtil.get_client(mongo_uri) as client:
            database = MongoDBUtil.get_database(client, 'users')
            return MongoDBUtil.update_one(database, 'user_profiles', {'_id': user_id}, user_update_data)

    def delete_user(self, mongo_uri, user_id):
        with MongoDBUtil.get_client(mongo_uri) as client:
            database = MongoDBUtil.get_database(client, 'users')
            return MongoDBUtil.delete_one(database, 'user_profiles', {'_id': user_id})
