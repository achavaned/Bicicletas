from flask import Flask
from flask_pymongo import pymongo
from app import app
CONNECTION_STRING = "mongodb+srv://antoinecdc:9pnYjt0I5uBdl2Jf@clusterbici.ici19qz.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('bicicletas')
user_collection = pymongo.collection.Collection(db, 'user_collection')