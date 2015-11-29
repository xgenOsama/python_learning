import socket
import sys



HOST = '127.0.0.1'
PORT = 4444

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print 'our socket is created'

try:
	s.bind((HOST,PORT))
except socket.error as e :
	print 'error in binding port'
	sys.exit()

s.listen(20)

print 'Server is in listen mode now'

while 1:
	conn, addr = s.accept()
	print 'Connect with the : ' + addr[0] + ":" + str(addr[1])

s.close()