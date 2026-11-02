
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json


class Handler(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/user":
            params = parse_qs(parsed.query)
            user_id = params.get("id", [""])[0]

            if user_id == "1001":
                self.send_json(200, {
                    "code": 200,
                    "message": "success",
                    "data": {
                        "id": 1001,
                        "username": "admin"
                    }
                })
            else:
                self.send_json(404, {
                    "code": 404,
                    "message": "user not found"
                })
        else:
            self.send_json(404, {
                "message": "endpoint not found"
            })

    def do_POST(self):
        if self.path != "/login":
            self.send_json(404, {
                "message": "endpoint not found"
            })
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length)
            data = json.loads(body)
        except (ValueError, UnicodeDecodeError):
            self.send_json(400, {
                "message": "invalid JSON"
            })
            return

        if not isinstance(data, dict):
            self.send_json(400, {
                "message": "JSON object required"
            })
            return

        if (data.get("username") == "admin"
                and data.get("password") == "123456"):
            self.send_json(200, {
                "code": 200,
                "message": "login success"
            })
        else:
            self.send_json(401, {
                "code": 401,
                "message": "invalid credentials"
            })


server = HTTPServer(("127.0.0.1", 8000), Handler)
print("API server running on port 8000", flush=True)
server.serve_forever()
