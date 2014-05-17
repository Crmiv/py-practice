#!/usr/bin/env python

import os, time

print "first pid is", os.getpid()
if os.fork():
	print "from the parent" ,os.getpid()
else:
	print "from the kid" ,os.getpid()

time.sleep(1)
print "from all"

'''print pid
if pid:
	while(1):
		print"aa"
else:
	while(1):
		print"bb"
'''		
