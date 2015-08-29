import sys, BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
'''
    to have you own server you must have a handler from SimpleHttpServer
    Server from BaseHttpServer.httpserver
    protocol = 'http/1.0'

'''
Handler = SimpleHTTPRequestHandler
Server = BaseHTTPServer.HTTPServer
protocol = 'HTTP/1.0'

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

server_address = ('127.0.0.1', port)

Handler.protocol_version = protocol
httpd = Server(server_address,Handler)
#sa = httpd.socket.getsockname()
print 'Serving Http'
httpd.serve_forever()