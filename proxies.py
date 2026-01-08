from http.server import HTTPServer, BaseHTTPRequestHandler


HOST = "192.168.56.1"
PORT = 9999


class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        
        self.send_response(200)

        
        self.send_header("Content-type", "text/html")
        self.end_headers()

        
        self.wfile.write(
            bytes("<html><body><h1>HELLO</h1></body></html>", "utf-8")
        )


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), NeuralHTTP)
    print("Server now running...")

    try:
        server.serve_forever()  
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
        server.server_close()
