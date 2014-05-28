#!/usr/bin/env python
from HTMLParser import HTMLParser
#handle entity like &amp
from htmlentitydefs import entitydefs
import sys

class TitleParser(HTMLParser):
	def __init__(self):
		self.taglevels = []
		self.handledtags = ['title', 'ul', 'li']
		self.processing = None
		HTMLParser.__init__(self)
	
	def handle_starttag(self, tag, attrs):
		if len(self.taglevels) and self.taglevels[-1] == tag:
			self.handle_endtag(tag)
		
		self.taglevels.append(tag)
		if tag in self.handledtags:
			self.data = ''
			self.processing = tag
			if tag == 'ul':
				#do print

	def handle_data(self, data):
		if self.processing:
			self.title += data
	
	def handle_endtag(self, tag):
		if not tag in self.taglevels:
			return

		while len(self.taglevels):
			starttag = self.taglevels.pop()

			if starttag in self.handledtags:
				self.finishprocessing(starttag)

			if starttag == tag:
				break

	def cleanse(self):
		self.data = re.sub('\s+', ' ', self.data)

	def finishprocessing(self, tag):
		self.cleanse()
		if tag == 'title' and tag == self.processing:
			print "Dom title", self.data
		elif tag == 'ul':
			print "List ended"
		elif tag == 'li' and tag == self.processing:
			print "List item", self.data
		self.processing = None

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

