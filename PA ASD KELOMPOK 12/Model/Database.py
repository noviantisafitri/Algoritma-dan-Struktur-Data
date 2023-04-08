from pymongo import MongoClient


class Database:
    def __init__(self):

        client = MongoClient("mongodb+srv://noviantis112:21november@cluster1.nsfjyfw.mongodb.net/?retryWrites=true&w=majority")
        database = client["PA-ASD-KELOMPOK12"]
        
        self.akun_collection = database["akun"]
        self.data_collection = database["data"]