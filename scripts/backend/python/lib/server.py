from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytearray('Hello World!', 'utf-8'))

def main(PORT):
    my_httpserver = HTTPServer(('', PORT), MyHTTPRequestHandler)
    my_httpserver.serve_forever()


if __name__ == "__main__":
    main(8000)
