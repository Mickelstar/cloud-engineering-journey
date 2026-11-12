import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import sys

DAY18_DIR = "/app/day18"
sys.path.insert(0, DAY18_DIR)

from detector import analyze_url


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404, "Not Found")
            return

        response = json.dumps({"status": "ok"}).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_POST(self):
        if urlparse(self.path).path != "/analyze":
            self.send_error(404, "Not Found")
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))

            if length <= 0 or length > 4096:
                self.send_error(400, "Invalid request size")
                return

            body = self.rfile.read(length)
            payload = json.loads(body)

            if not isinstance(payload, dict):
                self.send_error(400, "Expected a JSON object")
                return

            url = payload.get("url")

            if not isinstance(url, str) or not url.strip():
                self.send_error(400, "Expected a non-empty string field named url")
                return

            result = analyze_url(url)

            if result.get("verdict") == "invalid":
                self.send_error(400, "Invalid URL")
                return

            response = json.dumps(result).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

        except (json.JSONDecodeError, ValueError):
            self.send_error(400, "Invalid request")

    def log_message(self, format, *args):
        print(f"HTTP {args[1]}")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Detector API listening on port 8080")
    server.serve_forever()