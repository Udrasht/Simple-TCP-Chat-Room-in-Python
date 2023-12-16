import socket
import threading
HEADER=64
PORT =5050
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"


# SERVER="127.0.0.1"
SERVER=socket.gethostbyname(socket.gethostname())
print(SERVER)
print(socket.gethostname())
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
def habdel_client(conn,addr):
    print(f"[NEW CONNECTION]{addr} connected.")
    connected =True
    while connected:
        msg_length=0
        msg_length=conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            print()
            print()
            print(msg_length)
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if(msg==DISCONNECT_MESSAGE):
                connected=False
            print(f"[{addr}]{msg}")
    conn.close()



def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr=server.accept()
        thread = threading.Thread(target=habdel_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount()-1}")

print("[STARTING] server is starting...")
start()

# if __name__=="__main__":