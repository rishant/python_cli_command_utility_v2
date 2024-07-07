# utils/mongodb_util.py

from pymongo import MongoClient


class MongoDBUtil:
    @staticmethod
    def get_client(uri):
        return MongoClient(uri)

    @staticmethod
    def get_database(client, db_name):
        return client[db_name]

    @staticmethod
    def insert_one(database, collection_name, document):
        collection = database[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    @staticmethod
    def upsert_one(database, collection_name, query, document):
        collection = database[collection_name]
        result = collection.update_one(query, {'$set': document}, upsert=True)
        return result.upserted_id if result.upserted_id else result.modified_count

    @staticmethod
    def find_one(database, collection_name, query):
        collection = database[collection_name]
        return collection.find_one(query)

    @staticmethod
    def update_one(database, collection_name, query, update_data):
        collection = database[collection_name]
        result = collection.update_one(query, {'$set': update_data})
        return result.modified_count

    @staticmethod
    def delete_one(database, collection_name, query):
        collection = database[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count
