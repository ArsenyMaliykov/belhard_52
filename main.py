import pymongo


client = pymongo.MongoClient('localhost', 27017)
database = client.belhard
collections = database.belhard
