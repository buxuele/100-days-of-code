from http import server
import socketserver

"""example:
python -m http.server 8000 --bind 127.0.0.1
python -m http.server --directory /tmp/
"""

PORT = 5000
Handler = server.SimpleHTTPRequestHandler

"""serve at current directory """
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port: ", PORT)
    httpd.serve_forever()




