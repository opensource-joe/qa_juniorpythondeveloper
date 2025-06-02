###############################################################################
# Python WSGI Application - Challenge I
###############################################################################
# A reference implementation of the WSGI specification.
# Not to be used in production environments.
from wsgiref.simple_server import make_server

###############################################################################
'''
Assignment:

Create a basic "Hello, World!" WSGI app:

  1.) Create a WSGI application named: app
 

  2.) The response should:
      - Set the HTTP status of:                   '200 OK' 
      - Set the 'Content-Type' header value of:   'text/plain'
      - Set the response body to:                 b'Hello, World!'
'''
# Add WSGI app below
###############################################################################
def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello, World!']
# End WSGI app
###############################################################################

if __name__ == '__main__':
    # Create a server and run the app until the process is terminated.
    server = make_server('', 5000, app)
    server.serve_forever()
    # Test for yourself as needed:
    # python3 playground/challenge_1.py
    # 
    # In another terminal use CURL to issue HTTP requests.
    # 
    # curl "http://localhost:5000/"
