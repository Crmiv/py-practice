#!/usr/bin/env python
from BaseHTTPServer import HTTPServer , BaseHTTPRequestHandler
import time

starttime = time.time()


class RequestHandler(BaseHTTPRequestHandler):
	def _writeheaders(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
	
	def do_HEAD(self):
		self._writeheaders()
	
	def do_GET(self):
		self._writeheaders()
		self.wfile.write("""<HTML><HEAD><TITLE>Sample Page</TITLE></HEAD><BODY>this is a sample html page</BODY></HTML>""")

serveraddr = ('', 8765)
srvr = HTTPServer(serveraddr, RequestHandler)
srvr.serve_forever()

