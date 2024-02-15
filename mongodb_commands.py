from pymongo import MongoClient
from constants import mongodb_url
# import pprint

client = MongoClient(mongodb_url)
db = client.wall
collection = db.post


def create_post(post):
    collection.insert_one(post)


# def read_posts(username):
#     return list(collection.find({'username':username},{'_id':0,'username':0}))


def read_posts(title):
    return list(collection.find({'title':title},{'_id':0}))


def get_message_count(username):
    messagecount = collection.count_documents({'username':username})
    return messagecount


# if __name__ == '__main__':
#     print(get_message_count('c'))