from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter():
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:37571/test?authSource=AAC' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    def read(self, data):
        cursor = self.database.animals.find(data, {"_id": False})
        
        return cursor
    
    def readAll(self, data=None):
        if data:
            cursor = self.database.animals.find(data, {"_id": False})
        else:
            cursor = self.database.animals.find({}, {"_id": False})
     
        return cursor
 
 # Method to impelement the U in CRUD.
    def update(self, data):
        if data is not None:
            if data:
                newData = self.database.animals.insert_one(data)
                print(newData)
                
            return newData
        else:
            raise Exception("Nothing to change")
            
 # Method to implement the D in CRUD.

    def delete(self, data):
        if data is not None:
            if data:
                result = self.database.animals.delete_one(data)
                print(result)
        else:
            raise Exception("No data to delete")