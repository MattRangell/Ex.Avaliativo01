import pymongo

class MotoristaDAO:
    def __init__(self, database):
        self.client = pymongo.MongoClient()
        self.database = self.client[database]
        self.collection = self.database["motorista"]

    def createMotorista(self, motorista):
        document = {
            "nome": motorista.getNome(),
            "idade": motorista.getIdade(),
            "cnh": motorista.getCnh()
        }
        try:
            self.collection.insert_one(document)
        except pymongo.errors.PyMongoError as e:
            print(e)

    def readMotorista(self, id):
        query = {"_id": id}
        try:
            result = self.collection.find_one(query)
            if result:
                nome = result["nome"]
                idade = result["idade"]
                cnh = result["cnh"]
                return Motorista(id, nome, idade, cnh)
        except pymongo.errors.PyMongoError as e:
            print(e)
        return None

    def updateMotorista(self, motorista):
        query = {"_id": motorista.getId()}
        new_values = {"$set": {
            "nome": motorista.getNome(),
            "idade": motorista.getIdade(),
            "cnh": motorista.getCnh()
        }}
        try:
            self.collection.update_one(query, new_values)
        except pymongo.errors.PyMongoError as e:
            print(e)

    def deleteMotorista(self, id):
        query = {"_id": id}
        try:
            self.collection.delete_one(query)
        except pymongo.errors.PyMongoError as e:
            print(e)