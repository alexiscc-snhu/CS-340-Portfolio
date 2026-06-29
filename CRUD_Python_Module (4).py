from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Connection Variables
        USER = 'aacuser'
        PASS = 'AlexisCS3402026!'
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]

    # -------------------------
    # CREATE
    # -------------------------
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Error inserting document:", e)
                return False
        return False

    # -------------------------
    # READ
    # -------------------------
    def read(self, query):
        if query is not None:
            try:
                data = self.collection.find(query, {"_id": False})
                return list(data)
            except Exception as e:
                print("Error reading data:", e)
                return []
        return []

    # -------------------------
    # UPDATE
    # -------------------------
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": new_values}
                )
                return result.modified_count
            except Exception as e:
                print("Error updating data:", e)
                return 0
        return 0

    # -------------------------
    # DELETE
    # -------------------------
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Error deleting data:", e)
                return 0
        return 0