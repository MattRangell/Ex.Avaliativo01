from pymongo import MongoClient


client = MongoClient('mongodb+srv://root:root@cluster0.kd794t7.mongodb.net/')


db = client['ExAvaliativo01']


motoristas_collection = db['Motoristas']


document = {
    'Corridas': [
        {
            'note': 4.5,
            'distance': 10,
            'price': 20,
            'Passageiro': {
                'document': '123456789',
                'name': 'John Doe'
            }
        },
        {
            'note': 3.8,
            'distance': 15,
            'price': 25,
            'Passageiro': {
                'document': '987654321',
                'name': 'Jane Smith'
            }
        },
        
    ]
}

motoristas_collection.insert_one(document)


client.close()
