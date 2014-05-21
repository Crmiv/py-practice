#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import time

#
from SocketServer import ThreadingMixIn

#use forking
import threading

starttime = time.time()
class RequestHandler(BaseHTTPRequestHandler):
	def _writeheaders(self, doc):
		#write http headers ,if there's no document, 
		#send 404 error code;otherwise send a 200 success code
		if doc is None:
			self.send_response(404)
		else :
			self.send_response(200)
	
	self.send_header('Content-type','text/html')
	self.end_headers()

	def _getdoc(self, filename):
		global starttime
		if filename == '/':
			#print a html page
		
		elif filename == '/stats.html':
			#different page to show the time

	def do_HEAD(self):
		doc = self._getdoc(self, path)
		self._writeheaders(doc)
	def do_GET(self):
		doc = self._getdoc(self.path)
		self._writeheaders(doc)
		if doc is None:
			self.wfile.write("""<html></html>""")
		else:
			self.wfile.write(doc)
class ThreadHTTPServer(ThreadingMixIn, HTTPServer):
	pass


serveraddr = ('',4321)
srvr = HTTPServer(serveraddr, RequestHandler)
#use forking
#srvr = ThreadHTTPServer(serveraddr, RequestHandler)
srvr.serve_forever()


