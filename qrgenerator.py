import webbrowser
from http.server import BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "<h1> Hii this is a test message from server </h1>"
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        print("This is a post request");
        content_length = int(self.headers['Content-Length'])
        # <--- Gets the data itself
        post_data = self.rfile.read(content_length)
        stringurl = post_data.decode("utf-8")
        webbrowser.open_new(stringurl)
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        message = "saral share qr scanned!"
        self.wfile.write(bytes(message, "utf8"))




# print(IPAddr)
# def startServer(label):
    


