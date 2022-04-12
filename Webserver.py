# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

import settings
hostName = settings.get()[0]
serverPort = settings.get()[1]
fileRoot = settings.get()[2]
systemType = settings.get()[3]

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/'):
            self.path += 'index.html'
        
        try:
            if systemType == "Windows":
                requestedFile = open(fileRoot + self.path.replace('/','\\'), 'r')
            else:
                requestedFile = open(fileRoot + self.path, 'r')
                
        except:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes('<p>Http error 404: Page not Found. <button type="button" onclick="window.open(\'mailto:mwohkiller@gmail.com\')">Click to email Server owner</button></p>', "utf-8"))
            return

        try:
            if self.path.endswith('.html'):
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(requestedFile.read(), "utf-8"))
                requestedFile.close()
        except:
            self.send_response(500)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes('<p>Http error 500: Intertnal Server Error. <button type="button" onclick="window.open(\'mailto:mwohkiller@gmail.com\')">Click to email Server owner</button></p>', "utf-8"))
    def do_POST(self):
        print(self)
    
    
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
