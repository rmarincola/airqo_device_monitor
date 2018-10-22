from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

class MalfunctioningChannels(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/json')
		self.end_headers()
		self.wfile.write("{'hi': 'hello'}")
