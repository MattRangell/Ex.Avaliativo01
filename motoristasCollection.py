# Import the required libraries
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb+srv://root:root@cluster0.kd794t7.mongodb.net/')

# Switch to your desired database
db = client['ExAvaliativo01']

# Create a collection named "Motoristas"
motoristas_collection = db['Motoristas']

# Define the document to be inserted
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
        # Add more instances of "Corridas" if needed
    ]
}

# Insert the document into the collection
motoristas_collection.insert_one(document)

# Close the connection
client.close()