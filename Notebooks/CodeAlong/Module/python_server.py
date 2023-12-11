from http.server import HTTPServer, SimpleHTTPRequestHandler


def run_http_server():
    httpd = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    print("Running HTTP server on port 8000...")
    print("Open http://localhost:8000 in your browser.")
    print("Press Ctrl-C to stop.")
    run_http_server()
