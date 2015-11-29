import socket
import sys



HOST = '127.0.0.1'
PORT = 4444

cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cs.connect((HOST,PORT))
cs.send('Hello')