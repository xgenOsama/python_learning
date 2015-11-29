import socket
import sys



HOST = '127.0.0.1'
PORT = 4444

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))

s.listen(5)

while 1:
	connection, address = s.accept()
	buf = connection.recv(64)
	if len(buf) > 0:
		print buf
		break