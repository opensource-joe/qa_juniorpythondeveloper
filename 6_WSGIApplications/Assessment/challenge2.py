###############################################################################
# Python WSGI Application - Challenge II
###############################################################################
# A reference implementation of the WSGI specification.
# Not to be used in production environments.
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

themes = {
    "light":    ('FFF8DC', '000000'),
    "dark":     ('2F4F4F', 'FFF8DC'),
    "nature":   ('008B8B', 'FFFFFF'),
    "default":  ('6495ED', 'FFFFFF'),
}

def app(environ, start_response):
    ''' app is a basic WSGI application that yields a str representation of the
        theme's tuple of color codes.

       Example output:
        "('FFF8DC', '000000')"      
    '''
    start_response('200 OK', [('Content-Type', 'text/plain')])
    theme = environ.get('THEME', 'default')
    # The encode method is used to convert a str object into a bytestring.
    yield f'{themes[theme]}'.encode()

###############################################################################
'''
Assignment:

Create middleware to wrap the above app function:

  1.) The middleware must parse the query string and extract the optional
      parameter named: theme. 
      - Example query string: localhost:5000/?theme=nature

  2.) Assign the theme to the middleware's environ dictionary 
      with a key named: THEME.
      - Assign the value of None if no theme is provided in the query string. 
  
  3.) Assign your middleware to the theme_middleware name binding below.
       - NOTE: Challenge validation attempts will fail if this step is omitted.
       - Example: 
          >>> theme_middleware = ThemeMiddleware

'''
# Add middleware below
###############################################################################


# End middleware
###############################################################################
# Assign your middleware to this name binding.
theme_middleware = None


if __name__ == '__main__':
    # Create a server and run the app until the process is terminated.
    server = make_server('', 5000, theme_middleware(app))
    server.serve_forever()
    # Test for yourself as needed:
    # python3 playground/challenge_2.py
    # 
    # In another terminal use CURL to issue HTTP requests.
    # 
    # curl "http://localhost:5000/?theme=nature"
