from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir
import cgi
import keyCommands
import socket

class RequestHandler(BaseHTTPRequestHandler):
	def parse_POST(self):
		ctype, pdict = cgi.parse_header(self.headers['content-type'])
		if ctype == 'multipart/form-data':
			postvars = cgi.parse_multipart(self.rfile, pdict)
		elif ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers['content-length'])
			postvars = parse_qs(
				self.rfile.read(length),
				keep_blank_values=1
				)
		else:
			postvars = {}

		return postvars

	def do_POST(self):
		postvars = self.parse_POST()
		
		if postvars:
			self.send_response(200)
			self.end_headers()

		if b'position' in postvars.keys():
			rel_pos = tuple(postvars[b'position'][0].decode('ascii').split(","))
			keyCommands.do_move(rel_pos)

		if b'key' in postvars.keys():
			direction = postvars[b'key'][0].decode('ascii')
			keyCommands.do_press(direction)

		if b'scroll' in postvars.keys():
			scroll_amount = postvars[b'scroll'][0].decode('ascii')

		if b'click' in postvars.keys():
			keyCommands.do_click()

		if b'type' in postvars.keys():
			text = postvars[b'type'][0].decode('utf-8')
			keyCommands.do_type(text)

		if b'specialK' in postvars.keys():
			key = postvars[b'specialK'][0].decode('ascii')
			up_down = int(postvars[b'up_down'][0].decode('ascii'))
			keyCommands.do_special_key(key, up_down)

	def do_GET(self):
		
		raw_request = self.raw_requestline.decode('ascii')[6:-11].split('&')

		postvars = {}
		try:
			for x in raw_request:
				var,value = x.split("=")
				var, value = var.encode('ascii'), [value.encode('ascii')]
				postvars[var] = value
		except ValueError:
			pass

		
		if postvars:
			self.send_response(200)
			self.end_headers()
		else:
			if self.path == "/":
				self.path = "/index.html"
			elif not "." in self.path:
				self.path += ".html"
			try:
				sendReply = False
				if self.path.endswith(".html"):
					mimetype = "text/html"
					sendReply = True
				if self.path.endswith(".jpg"):
					mimetype='image/jpg'
					sendReply = True
				if self.path.endswith(".jpeg"):
					mimetype = 'image/jpeg'
					sendReply = True
				if self.path.endswith(".gif"):
					mimetype='image/gif'
					sendReply = True
				if self.path.endswith(".js"):
					mimetype='application/javascript'
					sendReply = True
				if self.path.endswith(".css"):
					mimetype='text/css'
					sendReply = True
				
				if sendReply == True:
					#Open the static file requested and send it
					f = open(curdir + "/" + self.path,'rb') 
					self.send_response(200)
					self.send_header('Content-type',mimetype)
					self.end_headers()
					self.wfile.write(f.read())
					f.close()

				return

			except IOError:
				self.send_error(404, "File Not Found: %s" % self.path)

		if b'position' in postvars.keys():
			rel_pos = tuple(postvars[b'position'][0].decode('ascii').split(','))
			rel_pos = (int(rel_pos[0]), int(rel_pos[1]))
			keyCommands.do_move(rel_pos)

		if b'key' in postvars.keys():
			key = postvars[b'key'][0].decode('ascii')
			keyCommands.do_press(key)

		if b'scroll' in postvars.keys():
			scroll_amount = postvars[b'scroll'][0].decode('ascii')
			keyCommands.do_scroll(scroll_amount)

		if b'click' in postvars.keys():
			keyCommands.do_click()

		if b'type' in postvars.keys():
			text = postvars[b'type'][0].decode('utf-8')
			keyCommands.do_type(text)

		if b'specialK' in postvars.keys():
			key = postvars[b'specialK'][0].decode('ascii')
			up_down = int(postvars[b'up_down'][0].decode('ascii'))
			keyCommands.do_special_key(key, up_down)

def httpd():
	RequestHandlerClass = RequestHandler
	server = HTTPServer(('0.0.0.0', 8000), RequestHandlerClass)

	try:
		server.serve_forever()
	except Exception as e:
		pass

	server.server_close()

def main():
	httpd()

if __name__ == '__main__':
	main()
