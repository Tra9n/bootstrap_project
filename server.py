from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class ContactServer(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open("contacts.html", "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            self.send_error(404, "File not found")
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(content.encode("utf-8"))

if __name__ == "__main__":
    host, port = "localhost", 5000
    server = HTTPServer((host, port), ContactServer)
    print(f"Сервер запущен на http://{host}:{port}")
    print("На любой GET-запрос отдаётся contacts.html. Ctrl+C для выхода.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
        server.server_close()