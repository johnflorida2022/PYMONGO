import pymongo  
from pymongo import MongoClient



cluster = MongoClient("mongodb+srv://johnr:admin@cluster0.isvrbfp.mongodb.net/?retryWrites=true&w=majority")
db = cluster["pytech"]
collection = db["students"]

collection.insert_one({"_id":1001, "user_name":"john"})

print(db.list_collection_names()) # print(db.list_collection_names)











