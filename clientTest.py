import socket

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

def menu():
    print("Welcome to the server!\nOptions:\n1. Roll for Characters\n0. Exit")   

def submenu():
    print("--------------------------------")
    print("\n1. Roll Again\n2.Back to Menu")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)
client_socket.connect(server_address)
data = client_socket.recv(1024).decode()
user = input("Please enter your username: ")
client_socket.send(user.encode())

print(data)
menu()
message = 'temp'

while (message != '0'):
    message = input(" -> ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    if(message == '1'):
        convertMessage(data)
        submenu()
        message = input(" -> ")
        if(message == '2'):
            menu()
            continue

client_socket.close()
