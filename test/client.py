#!/bin/python
import socket

s = socket.socket()

host = '218.244.136.182' 
port = 8001

s.connect((host, port))
print s.recv(1024)
