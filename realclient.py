import socket 
import select 
import sys 
import time
import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sys.argv.append("127.0.0.1")#IP ADDRESS
sys.argv.append(25565)#PORT
if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number")
	exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 
s = input()
server.send(s.encode())
print(server.recv(2048).decode("utf-8",'ignore'))
