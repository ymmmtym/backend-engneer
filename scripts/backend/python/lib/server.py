from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytearray('Hello World!', 'utf-8'))

def main():
    my_httpserver = HTTPServer(('0.0.0.0', 8000), MyHTTPRequestHandler)
    my_httpserver.serve_forever()
    my_httpserver.server_close() 


if __name__ == "__main__":
    main()
