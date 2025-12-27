from pymongo import MongoClient

from pymongo import MongoClient

DB_URI = "mongodb://admin:admin@127.0.0.1:27017/langgraph?authSource=admin"

client = MongoClient(DB_URI)
print(client.list_database_names())



