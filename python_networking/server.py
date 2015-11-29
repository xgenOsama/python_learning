import socket



sock = socket.socket()


host = socket.gethostbyname()
port = 4444

sock.bind(host,port)

sock.listen(20)

while True:
	c, addr = sock.accept()
	print 'i am getting connection from : ', addr
	c.send('You are good client')
	c.close()