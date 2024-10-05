from pymongo import MongoClient

def get_mongo_client():
    mongo_uri = "mongodb+srv://intelli_test:srgsliit123@testcluster.xm1be.mongodb.net/?retryWrites=true&w=majority&appName=TestCluster"
    client = MongoClient(mongo_uri)
    return client
