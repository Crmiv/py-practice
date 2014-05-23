#!/usr/bin/env python
from SocketServer import ThreadingMixIn, TCPServer, StreamRequestHandler
import time
class TimeRequestHandler(StreamRequestHandler):
	def handle(self):
		req = self.rfile.readline().strip()
		if req == "asctime":
			result = time.asctime()
		elif req == "seconds":
			result = str(int(time.time()))
		else:
			result = "Please enter time-type"
		self.wfile.write(result+'\n')

class TimeServer(ThreadingMixIn, TCPServer):
	allow_reuse_address = 1
	
if __name__=='__main__':
	serveraddr = ('',5555)
	serv = TimeServer(serveraddr,TimeRequestHandler)
	serv.serve_forever()

