#!/usr/bin/env python
import sys
from time import sleep
f = sys.stdout
for i in range(10):
	f.write("***")
	sleep(0.5)
	f.flush()
