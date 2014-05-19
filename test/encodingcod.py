#!/usr/bin/env python

import struct, sys

def ht(num):
	return struct.pack('!H', num)
def lt(num):
	return struct.pack('!I', num)

a = 12113
x = ht(a)
y = lt(a)
print x
