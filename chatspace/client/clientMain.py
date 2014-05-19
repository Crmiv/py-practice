#!/usr/bin/env python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("218.244.136.182",80))

