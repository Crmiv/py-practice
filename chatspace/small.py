from asyncore import dispatcher
import asyncore
import socket

class ChatServer(dispatcher): 
	def handle_accept(self):
		conn, addr = self.accept()
		print "conn from add ", addr[0]
	
s = ChatServer()
s.create_socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',5005))
s.listen(5)
asyncore.loop()

