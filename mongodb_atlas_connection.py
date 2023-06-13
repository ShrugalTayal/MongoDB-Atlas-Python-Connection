"""
Reference: Connecting to MongoDB Atlas with Python (PyMongo)

This code demonstrates the process of connecting to a MongoDB Atlas cluster using Python and PyMongo. It follows the steps outlined in the Medium article titled "Connecting to MongoDB Atlas with Python (PyMongo)".

Article Link: [Connecting to MongoDB Atlas with Python (PyMongo)](https://medium.com/analytics-vidhya/connecting-to-mongodb-atlas-with-python-pymongo-5b25dab3ac53)

Prerequisites:
- Install the PyMongo package by running 'pip install pymongo' in your Python environment.
- Set up a MongoDB Atlas account and create a cluster.

Usage:
1. Replace the 'uri' variable with your own MongoDB Atlas connection string.
2. Run the code to establish a connection with your MongoDB Atlas cluster.
3. Ensure that the connection is successful by checking the printed message.

Note: This code assumes you have already installed the necessary dependencies and have a valid MongoDB Atlas cluster set up.
"""

import pymongo
from pymongo import MongoClient

# MongoDB connection string
uri = "mongodb+srv://your-connection-string"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Accessing a specific database
db = client["YourDatabase"]
print(db)

# Accessing a specific collection within the database
collection = db["YourCollection"]
print(collection)

# Inserting a single document
collection.insert_one({"_id": 0, "user_name": "YourName"})

# Inserting multiple documents
collection.insert_many([
    {"_id": 100, "user_name": "AnotherName"},
    {"_id": "101", "user_name": "YetAnotherName"}
])

# Deleting a document
collection.delete_one({"_id": 0, "user_name": "YourName"})

# Updating a document
collection.find_one_and_update(
    {"_id": "0"},
    {"$set": {"user_name": "updated_user_name"}},
    upsert=False
)
