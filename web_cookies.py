
import webapp2
from paste import httpserver
import random


def GetAllHeaders(headers):
	header_response = "HTTP Header Recieved \n"
	for k, v in headers.items():
		header_response += "%s : %s \n" % (v, k)

	return header_response


class RootCookie(webapp2.RequestHandler):
	"""docstring for RootCookie"""
	def get(self):
		self.response.content_type = "text/plain"
		header_response = GetAllHeaders(self.request.headers)


		#Not checking if cookie value is preset , simple overwrite existing

		self.response.set_cookie(
				'root_session_id',
				str(random.getrandbits(128)),
				max_age = 1200,
				path = "/"
			)


		self.response.set_cookie(
				'blog_session_id',
				str(random.getrandbits(128)),
				max_age = 1200,
				path = "/blog"
			)

		self.response.write(header_response)

class BlogCookie(webapp2.RequestHandler):
    
    def get(self):
        self.response.content_type = "text/plain"
        header_response = GetAllHeaders(self.request.headers)
        self.response.write(header_response)


class ForumCookie(webapp2.RequestHandler):
    
    def get(self):
        self.response.content_type = "text/plain"
        header_response = GetAllHeaders(self.request.headers)
        self.response.write(header_response)


class BlogginCookie(webapp2.RequestHandler):
    
    def get(self):
        self.response.content_type = "text/plain"
        header_response = GetAllHeaders(self.request.headers)
        self.response.write(header_response)


app = webapp2.WSGIApplication([
                ("/",RootCookie),
                ('/blog',BlogCookie),
                ('/bloggin',BlogginCookie),
                ('/forum',ForumCookie),
            ],debug=True)

def StartServer():
    httpserver.serve(app,host= '0.0.0.0',port='8080')


if __name__ == "__main__":
    StartServer()
