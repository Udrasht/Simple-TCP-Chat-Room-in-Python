import socket
import threading
from colorama import Fore, Style
username=input("choose a username: ")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555))

def recive():
    while True:
        try:
            message=client.recv(1024).decode('ascii')
            if message =='USER_NAME:':
                client.send(username.encode('ascii'))
            else:
                print(Fore.GREEN + message+ Style.RESET_ALL)
        except:
            print(Fore.RED + "ERROR!"+ Style.RESET_ALL)
            client.close()
            break

def write():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('ascii'))
recive_thread=threading.Thread(target=recive)
recive_thread.start()
write_thread=threading.Thread(target=write)
write_thread.start()

