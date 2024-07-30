from pymongo import MongoClient
from createCharacter import *
import json

def convertMessage(str):
    print("**********************************\n")
    print("Your character is: \n")
    print("**********************************\n")
    name = str[str.index("\""):str.index(",")]
    str = str[str.index(",")+1:].strip()
    print("Name: " + name)
    health = str[:str.index(",")].strip()
    print("Health Points: " + health)
    str = str[str.index(",")+1:].strip()
    attack = str[:str.index(",")].strip()
    print("Attack: " + attack)
    str = str[str.index(",")+1:].strip()
    defence = str[:str.index(",")].strip()
    print("Defence: " + defence)
    str = str[str.index(",")+1:].strip()
    speed = str[:str.index("]")].strip()
    print("Speed: " + speed)
    
def convertCursorObject(cur):
    for a in cur:
        print("**************Character******************")
        print("Name: " + a["name"])
        print("Health Points: ", a["health"])
        print("Attack: ", a["attack"])
        print("Defence: ", a["defence"])
        print("Speed: ", a["speed"])
        print("****************************************")
        
def addCharacterToUser(login,name):
    myquery = { "login": login }
    newvalues = { "$push" : { "characters" : {"charName" : name} }}
    userCollection.update_one(myquery, newvalues)
    
def showAllCharacter(login):
    user1 = userCollection.find({"login" : login})
    for d in user1:
        for x in range(0, len(d["characters"])):
            found = characterCollection.find({"name" : (d["characters"][x]["charName"])})
            convertCursorObject(found)
    
def checkUser(login):
    if (userCollection.count_documents({ 'login': login }, limit = 1) == 0):
        user = {
            "login": login,
            "wins" : 0,
            "characters" : [{}]
        }
        print("New user created")
    else:
        print("Welcome Back " + login + "!")
    

connection_string = "mongodb+srv://akhabibulin00:yXIcMd9EibPoytmJ@cluster0.abkchr1.mongodb.net/"
dbconnection = MongoClient(connection_string)
db = dbconnection['cpsc1280']
characterCollection = db['characters']
userCollection = db['users']

# randCharacter = createCharacter()
# character = {
# "name": randCharacter[0],
# "health": randCharacter[1],
# "attack": randCharacter[2],
# "defence": randCharacter[3],
# "speed": randCharacter[4]
# }

# login=input("Enter Login: ")
# print(userCollection.count_documents({ 'login': login }, limit = 1) != 0)
# user = {
#     "login": login,
#     "wins" : 0,
#     "characters" : [{"charName" : randCharacter[0]}]
# }

# characterCollection.insert_one(character)
# addCharacterToUser("player1", randCharacter[0])

# userCollection.insert_one(user)
# user1 = userCollection.find({"login" : "player1"})
# for d in user1:
#     for x in range(0, len(d["characters"])):
#         found = characterCollection.find({"name" : (d["characters"][x]["charName"])})
#         convertCursorObject(found)
# print([randCharacter[0]])
# myquery = { "login": "player1" }
# newvalues = { "$push" : { "characters" : {"charName" : randCharacter[0]} }}
# userCollection.update_one(myquery, newvalues)
