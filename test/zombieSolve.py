#!/usr/bin/env python

import os, time, signal
def chldhandler(signum, stackframe):
	while 1:
		try:
			result = os.waitpid(-1, os.WHOHANG)
		except:
			break
		print "reaped child process %d " % result[0]
	signal.signal(signal.SIGCHLD, chldhandler)

#SIGCHLD belongs linux signal ,represent chld-process halt
signal.signal(signal.SIGCHLD,chldhandler)

print "before fork,pid" , os.getpid()
pid = os.fork()

if pid:
	print time.sleep(10)
else:
	time.sleep(5)

