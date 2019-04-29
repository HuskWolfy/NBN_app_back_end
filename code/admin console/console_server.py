#!/usr/bin/python
"""
Usage: ./dummy-web-server.py [<port>]

Send a GET request: curl http://localhost

Send a HEAD request: curl -I http://localhost

Send a POST request: curl -d "foo=bar&bin=baz" http://localhost
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class S(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		webpage = open("console.html","rb")
		self._set_headers()
		self.wfile.write(webpage.read())

	def do_HEAD(self):
		self._set_headers()
		
	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length)
		print(post_data)
		self._set_headers()
		self.wfile.write("<html><body><h1>200</h1>event sucessfully added</body></html>")

def run(server_class=HTTPServer, handler_class=S, port=3000):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print 'admin console server online'
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()
