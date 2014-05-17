#!/usr/bin/env python
import os, time

def reap():
	while(1):
		try:
			result = os.waitpid(-1,WHOHANG)	
		except:
			break
		print "Reaped child process %d" % result[0]

print "before fork my pid is " , os.getpid()

pid = os.fork()
if pid:
	print "Hello from the parent,child pid is %d" % pid
	time.sleep(60)
	reap()
	time.sleep(60)
else:
	time.sleep(5)


