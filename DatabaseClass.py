from pymongo import MongoClient

class Database:
    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.client = None
        self.db = None
    
    def connect(self):
        try:
            self.client = MongoClient(self.host, self.port)
            self.db = self.client[self.database]
            self.db.authenticate(self.username, self.password)
            print("Connected to database successfully")
        except Exception as e:
            print("Failed to connect to database:", str(e))
    
    def disconnect(self):
        if self.client is not None:
            self.client.close()
            print("Disconnected from database")    
    
    def insert_document(self, collection, document):
        try:
            self.db[collection].insert_one(document)
            print("Document inserted successfully")
        except Exception as e:
            print("Failed to insert document:", str(e))