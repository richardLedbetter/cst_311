import socket
import os
import select 
import sys 
from _thread import *
import datetime

import re


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sys.argv.append("127.0.0.1")#IP ADDRESS
sys.argv.append(25565)#PORT

IP_address = str(sys.argv[1]) 

Port = int(sys.argv[2])

server.bind((IP_address, Port)) 



server.listen(100) 


def clientthread(conn,addr):
	buff_size = 4096
	message = conn.recv(buff_size)	
	message = message.decode("utf-8",'ignore')
	print("from",addr[0],message)
	conn.send(message.upper().encode())

while True: 
	conn, addr = server.accept() 
	print(conn)
	print (addr[0] + " connected")
	start_new_thread(clientthread,(conn,addr))

conn.close() 
server.close() 

