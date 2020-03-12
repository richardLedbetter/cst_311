#multithreading is needed to handle the mutlitple connections 
import socket
from _thread import *


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("127.0.0.1",25565))
server.listen(100)
global first
first = "blank"
global count
count = 0
global connected
connected =0


def interface(conn,addr):
	global first
	global count
	global connected
	connected = connected +1
	c2 = count
	name = ""
	while(connected<1):
		continue
	message = conn.recv(2048)
	if( first =="blank"):
		first = message.decode("utf-8")+ " recived before"
	else:
		first = first+" " + message.decode("utf-8")
	count = count+1
	while(count<2):
		continue
	print("sending"+first+ "to connection" +str(c2))
	conn.send((first).encode())


while True:
	conn,addr = server.accept()
	start_new_thread(interface,(conn,addr))
