#!/usr/bin/env python
import socket , traceback, time

host = ''
port = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

while 1:
	try:
		clientsock, clientaddr = s.accept()
	except KeyboardError: 
		raise
	except:
		traceback.print_exc()
		continue

	try:
		print 'conn from', clientsock.getpeername()
		while 1:
			try:
				clientsock.sendall(time.asctime() + "\n")
			except:
				break
			time.sleep(5)
	except (KetboardError, SystemExit):
		raise
	except:
		traceback.print_exc()

	#Close conn

	try:
		clientsock.close()
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()

