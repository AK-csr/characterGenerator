from pymongo import MongoClient
from createCharacter import *
import json

def insertCharacterMongo():
  connection_string = "mongodb+srv://akhabibulin00:yXIcMd9EibPoytmJ@cluster0.abkchr1.mongodb.net/"
  dbconnection = MongoClient(connection_string)
  db = dbconnection['cpsc1280']
  collection = db['characters']
  
  randCharacter = createCharacter()
  character = {
    "name": randCharacter[0],
    "health": randCharacter[1],
    "attack": randCharacter[2],
    "defence": randCharacter[3],
    "speed": randCharacter[4]
  }
  collection.insert_one(character)
  return randCharacter


