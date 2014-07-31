#!usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

Deafult_www_path = "/var/www/index.html"
port_number = 8080

class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        #send the HTML message
        #Set /var/www/ as the default directory for web pages
        try:
            if(self.path == "/"):  
                file = open("/var/www/index.html", 'r')
                data = file.read()
                #search for index.html file in path and display it
                x = bytes(data, 'utf-8')
                file.close()
                self.wfile.write(x)
            
        except:
            if(self.path != "/"):
                self.get_request()
                x = bytes("Could not find default page in path", 'utf-8')
                self.wfile.write(x)
        return

try:

        #Create a webserver and define the handler to manage the incoming request
        try:
            ip = "127.0.0.5"
            server = HTTPServer((ip, port_number), myHandler)
            print("Started HTTP Webserver on port", port_number)
            print("Server: Linx HTTP Server v0.1 - Created by Alexandre Juca")
            print(".....May show wrong return I.P in requests")
            print("Waiting for incoming requests........")
            #Wait forever for incoming http requests
            server.serve_forever()
        except:
            
            print("Served address already in use")
            
        
            


except KeyboardInterrupt:
    print(" Recieved, Shuttinf down the web server")
    server.socket.close()
