from flask_pymongo import PyMongo
from app import app # // Modidied

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.database_name

# mongo = PyMongo() // Modified
mongo = PyMongo(app)
