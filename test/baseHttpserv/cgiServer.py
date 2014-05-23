#!/usr/bin/env python
from BaseHTTPServer import HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
from SocketServer import ForkingMixIn

class ForkServer(ForkingMixIn, HTTPServer):
	pass

addr = ('',5555)
serv = ForkServer(addr, CGIHTTPRequestHandler)
serv.serve_forever()

