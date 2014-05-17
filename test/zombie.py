#!/usr/bin/env python
import os, time
print os.getpid()
pid = os.fork()
if pid:
	time.sleep(100)
