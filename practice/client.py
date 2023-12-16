import socket
HEADER=64
PORT =5050
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER ="10.1.37.169"
ADDR=(SERVER,PORT)



client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
def send(msg1):
    message=msg1.encode(FORMAT)
    msg_length=len(message)
    print(msg_length)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' '*(HEADER-len(send_length))
    
    client.send(send_length)
    client.send(message)
send("hello iiit hyderabad i love my india")
send("hello  india")
send("hello  i love my india")
send("DISCONNECT_MESSAGE")