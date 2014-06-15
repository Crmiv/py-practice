#!/usr/bin/env python
import socket, time

#Server your client wanna to connect
SERVER_IP = ''
SERVER_PORT = '43278'
BEAT_PERIOD = 5
while True:
	hbSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	hbSocket.sendto('PyHB',(SERVER_IP,SERVER_PORT))
	if __debug__:
		print '%s ' Time.ctime()
		time.sleep(BEAT_PERIOD)
	

