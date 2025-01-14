import re
from http.server import BaseHTTPRequestHandler, HTTPServer

class app(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

    if re.search('/api/helloworld', self.path):
      message = "Hello, World"
      self.wfile.write(bytes(message, "utf8"))
      
    if re.search('/sasa', self.path):
      message = "ca ta sasa"
      self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8000), app) as server:
  server.serve_forever()