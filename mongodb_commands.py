from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.wall
collection = db.post


def create_post(post):
    collection.insert_one(post)