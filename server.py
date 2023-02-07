from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
  server_address = ("", 8000)
  httpd = server_class(server_address, handler_class)
  httpd.serve_forever()

class NoExtensionHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
    print("\n(GET) unmodified path:", self.path)
    self.path = directory + self.path
    print("(GET) with directory:", self.path)
    
    home_paths = ["/public/"]
    # The exclusion of paths with a period excludes image, js and other file types
    # We also exclude the "/" path since this servers index.html by default
    if self.path not in home_paths and not "." in self.path:
      self.path += ".html"
      print("(GET) extension added:", self.path)
    SimpleHTTPRequestHandler.do_GET(self)

# *** MAIN *** #

if len(sys.argv) == 1:
  directory = "/public"
  print(f"Serving from public directory...")
  run(HTTPServer, NoExtensionHandler)
# elif len(sys.argv) == 2:
#   flags = ["--docs", "--production"]

#   if sys.argv[1] in flags:
#     directory = "/docs"
#     print(f"Recieved '{sys.argv[1]}' flag, serving from /docs/ directory...")
#     run(HTTPServer, NoExtensionHandler)
#   else:
#     print(f"Invalid flag provided. Expected one of {str(flags)}, got '{sys.argv[1]}'")
else:
  print(f"Invalid number of arguments recieved. Expected none, got {len(sys.argv) - 1}")