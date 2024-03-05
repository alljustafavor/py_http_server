from http import server
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

class PyHTTPServer:

    def __init__(self, host_address='', port=8000):
        self.host_address = host_address
        self.port = port
        self._server = None

    def _create_req_handler(self):

        class PyReqHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("<html><body><h1>Hello!</h1></body></html>", "utf-8"))
                pass

        return PyReqHandler

    
    def start_server(self):
        handler_class = self._create_req_handler()
        print(handler_class)
        try:
            self._server = HTTPServer((self.host_address, self.port), handler_class)
            print(f"Starting HTTP server on {self.host_address} port {self.port} (http://{self.host_address}:{self.port}/)")
            self._server.serve_forever()
        except Exception as e:
            print("Error starting server:", e)


    def stop_server(self):
        if self._server:
            self._server.shutdown()
            self._server = None

if __name__ == '__main__':
    server = PyHTTPServer('localhost', 8000)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()

