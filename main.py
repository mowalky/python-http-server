from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "localhost"
PORT = 8888

class TestHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Hello Universe!</h1></body></html>", "utf-8"))

server = HTTPServer((HOST,PORT), TestHTTP)
print("Server now running ...")
server.serve_forever()
server.server_close()
print("Server stoppped!")