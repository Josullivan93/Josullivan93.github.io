import http.server
import socketserver

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # MANDATORY FOR WEBR
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    with socketserver.TCPServer(("", 8000), MyHTTPRequestHandler) as httpd:
        print("Serving at http://localhost:8000")
        httpd.serve_forever()