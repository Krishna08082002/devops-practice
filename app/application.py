import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            message = "DevOps application v2 is running!"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(message.encode())

        elif self.path == "/health":
            message = "OK"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(message.encode())

        else:
            self.send_response(404)
            self.end_headers()

PORT = int(os.environ.get("PORT", "8000"))

server = HTTPServer(("0.0.0.0", PORT), RequestHandler)

if __name__ == "__main__":
    print(f"Server running on port {PORT}...")
    server.serve_forever()
