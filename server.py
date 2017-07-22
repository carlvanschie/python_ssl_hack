from http.server import HTTPServer,SimpleHTTPRequestHandler
import ssl
import http.server


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(s):
        print("HEAD")
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        print("GET")
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write(bytes("YO GET", 'UTF-8'))

    def do_POST(s):
        print("POST")
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        print(s.rfile.read(int(s.headers.get("Content-Length"))))
        s.wfile.write(bytes("YO POST", 'UTF-8'))


httpd = HTTPServer(('localhost', 1443), MyHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='server.pem', server_side=True)
httpd.serve_forever() 

