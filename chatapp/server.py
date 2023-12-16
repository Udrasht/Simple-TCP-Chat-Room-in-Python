import socket
import threading
from colorama import Fore, Style
host='127.0.0.1'  #localhost
port=55555
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

#utilits
clients=[]
usernames=[]
def broadcast(message):
    for client in clients:
        client.send(message)
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            username=usernames[index]
            broadcast(f'{username} left the chat!'.encode('ascii'))
            usernames.remove(username)
            break

def recive():
    while True:
        client,address=server.accept()
        print(f"Connected with {str(address)}")
        client.send('USER_NAME:'.encode('ascii'))
        username=client.recv(1024).decode('ascii')
        usernames.append(username)
        clients.append(client)
        
        print(Fore.BLUE +f"usernames of client is {usernames}!"+ Style.RESET_ALL)
        broadcast(f'{username} joined the chat!'.encode('ascii'))
        client.send("Connected to server!".encode('ascii'))

        thread=threading.Thread(target=handle,args=(client,))
        thread.start()


print("server id lidtning...")
recive()




