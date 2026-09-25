import random
import string
from http.server import HTTPServer, BaseHTTPRequestHandler

class URLShortener:
    def __init__(self):
        self.urls = {}
        self.codes = {}
    def gen_code(self):
        while True:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k= 6))
            if code not in self.codes:
                return code
    def shorten(self, url):
        code = self.gen_code()
        self.urls[code] = url
        self.codes[url] = code
        return code
    def get_url(self, code):
        return self.urls.get(code)
    
shortener = URLShortener()

code = shortener.shorten(
    "https://shiiiivanshsingh.github.io/intro/"
)
    
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = shortener.get_url(self.path[1:])

        if url:
            self.send_response(302)
            self.send_header("Location", url)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Short URL not found")


server = HTTPServer(("localhost", 5000), Handler)

print(f"Short URL: http://localhost:5000/{code}")
print("Server running on http://localhost:5000")

server.serve_forever()
# if __name__ == "__main__":
#     s= URLShortener()
#     code = s.shorten("https://shiiiivanshsingh.github.io/intro/")
#     print(code)
#     print(s.get_url(code))