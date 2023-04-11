from pymongo import MongoClient


class Database:
    def __init__(self):

        client = MongoClient("mongodb://novianti:Ah7iRtN5AFbSnkYMLhDEgjAFeR5XxjQMCidRSQhE@sandbox-shard-00-00.u1rbk.mongodb.net:27017/?ssl=true")
        database = client["room_reserve"]
        
        self.akun_collection = database["akun"]
        self.data_collection = database["data"]
