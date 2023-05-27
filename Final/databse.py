from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class database():
    def __init__(self):
        self.uri = "mongodb+srv://Project_admin:Project_admin@maindata.7776kbd.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
        except:
            return "Connection Error"
        db = self.client["MainData"]
        self.collection = db['Login']
    
    def show(self):
        data = self.collection.find()
        for i in data:
            print(i)
        return "done"
    
    def insert(self, data):
        self.collection.insert_one(data)
        return 200
    
    def find(self, data):
        return self.collection.find_one(data)
    
    def update(self, query, data):
        self.collection.update_one(query, data)
        return 200

    
