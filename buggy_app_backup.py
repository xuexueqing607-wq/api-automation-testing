
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/login":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))

        try:
            data = json.loads(
                self.rfile.read(length).decode("utf-8")
            )
        except (ValueError, UnicodeDecodeError):
            self.reply(400, "invalid JSON")
            return

        username = data.get("username", "")
        password = data.get("password", "")

        # 故意留下的 Bug：只验证用户名
        if username == "admin":
            self.reply(200, "login success")
        else:
            self.reply(401, "invalid credentials")

    def reply(self, status, message):
        body = json.dumps({
            "code": status,
            "message": message
        }).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

server = HTTPServer(("127.0.0.1", 8001), Handler)
print("Buggy API running on port 8001", flush=True)
server.serve_forever()
