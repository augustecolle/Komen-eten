import BaseHTTPServer
import CGIHTTPServer

import cgitb; cgitb.enable()

server  = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_adress=("",9014)
handler.cgi_directories = ["/cgi-bin"]

httpd = server(server_adress, handler)
httpd.serve_forever()
