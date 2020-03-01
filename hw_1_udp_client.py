from socket import *
#import socket
import sys 
import time

#server connection
server = socket(AF_INET, SOCK_DGRAM)#creates listening socket
server.bind(('', 0))


#drop percentage variables
max = 0;
drop_count = 0;
min = 2;

#EstimatedRTT variables
alpha=.125
EstimatedRTT = 0
SampleRTT = 0

#devRtt variables
beta = .25
DevRtt = 0

for i in range (10):
	try:
		message = "ping"+str(i)
		#start timmer
		w = time.time()
		server.sendto(message.encode(), ('<broadcast>', 3000))
		server.settimeout(1)
		print("message:", server.recv(2048).decode())
		#get min max time
		t = time.time()-w
		if(max<t):
			max = t
		if(min>t):
			min = t
		#get EstimatedRTT
		SampleRTT = t
		EstimatedRTT = (1-alpha)*EstimatedRTT+(alpha*SampleRTT)
		print("took",t)
		#get devRTT
		DevRtt = (1-beta)*DevRtt +(beta*abs(SampleRTT-EstimatedRTT))
	except timeout:
		drop_count = drop_count+1
		print("Request timed out")


print()
print("============results===========")
print("max time:",max)
print("min time:",min)
print("packet loss percentage:",str(drop_count*10)+"%")
print("Estimated RTT:" , EstimatedRTT)
print("Dev RTT:", DevRtt)
print("Timeout Interval:" , EstimatedRTT + (4*DevRtt))
