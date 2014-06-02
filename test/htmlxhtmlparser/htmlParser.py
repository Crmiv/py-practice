#!/usr/bin/env python
from HTMLParser import HTMLParser
#handle entity like &amp
from htmlentitydefs import entitydefs
import sys

class TitleParser(HTMLParser):
	def __init__(self):
		self.title = ''
		self.readingtitle = 0
		HTMLParser.__init__(self)
	
	def handle_starttag(self, tag, attrs):

		if tag == 'script':
			self.readingtitle = 1 
	
	def handle_data(self, data):
		if self.readingtitle:
			self.title = data
	
	def handle_endtag(self, tag):
		if tag == 'script':
			self.readingtitle = 0

	def gettitle(self):
		return self.title
	
	def handle_entityref(self, name):
		if entitydefs.has_key(name):
			self.handle_data(entitydefs[name])
		else:
			self.handle_data('&' + name + ';')
	
	def handle_charref(self, name):
		try:
			charnum = int(name)
		except ValueError:
			return

		if charnum < 1 or charnum > 255:
			return

		self.handle_data(chr(charnum))
	

fd = open(sys.argv[1])
tp = TitleParser()
tp.feed(fd.read())
print tp.gettitle()

