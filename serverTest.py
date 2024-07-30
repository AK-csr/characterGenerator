import socket
import json
from createCharacter import *
from insertMongo import *
from userDB import *

def menu():
    return "Welcome to the server!\nOptions:\n1. Roll for Characters\n2. Manage Party\n0. Exit"

def submenu():
    return "1. Roll Again\n 2.Back to Menu"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)
server_socket.listen(5)

print('Server is listening on', server_address)

while True:
    client_socket, client_address = server_socket.accept()
    print('Connected to', client_address)
    message = "Connection Established!"
    client_socket.send(message.encode())
    username = client_socket.recv(1024).decode()
    checkUser(username)
    data = 'temp'
    
    while (data != '0'):
        data = client_socket.recv(1024).decode()
        if (data == '1'):
            print("Function PLAY:")
            character = insertCharacterMongo()
            addCharacterToUser(username, character[0])
            characterString = json.dumps(character)
            client_socket.send(characterString.encode())
        if(data == '2'):
            showAllCharacter(username)
        
    print("LOOP END POINT")
    client_socket.close()
print("BYE SERVER")