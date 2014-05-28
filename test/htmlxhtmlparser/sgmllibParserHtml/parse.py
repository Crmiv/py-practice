#!/usr/bin/env python
import sgmllib, urllib, urlparse
class Par(sgmllib.SGMLParser):
	def __init__(self):
		sgmllib.SGMLParser.__init__(self)
		self.seen = set()
	
	def do_a(self, attributes):
		for name, value in attributes:
			if name == 'href' and value not in self.seen:
				self.seen.add(value)
				self.seen.add(value)
				pieces = urlparse.urlparse(value)
				if pieces[0] != 'http': return
				print urlparse.urlunparse(pieces)
				return
	
p = Par()
f = urllib.urlopen('http://www.google.com')
BUFSIZE = 8192
while True:
	data = f.read(BUFSIZE)
	if not data: break
	p.feed(data)
p.close()

