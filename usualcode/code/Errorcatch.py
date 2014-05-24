#!/usr/bin/env python
import urllib, urllib2, sys
try:
		req = urllib2.Request(sys.argv[1])
		res = urllib2.urlopen(req)
except urllib2.URLError, e:
	print "error", e
	print e
	print e
	print e
