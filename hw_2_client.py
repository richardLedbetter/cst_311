import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.connect(("127.0.0.1", 25565)) 
message = input("enter your name:")
server.send(message.encode())
print("sent message")
print(server.recv(2048).decode("utf-8"))

