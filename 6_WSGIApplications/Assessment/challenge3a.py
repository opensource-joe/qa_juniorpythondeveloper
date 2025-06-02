###############################################################################
# Python WSGI Application - Challenge III
###############################################################################
import os
# A reference implementation of the WSGI specification.
# Not to be used in production environments.
from wsgiref.simple_server import make_server
from flask import Flask, request, render_template

class Messages:
    ''' Fake message storage. 

        Can add and get messages.

        In an attempt to keep things simple the default messages are just the 
        letter o repeated some number of times. 

        Example: 
        >>> messages = Messages()
        >>> messages.get(5)
        'ooooo'
        >>> messages.add(':)')
        >>> messages.get(10)
        ':)'
    '''
    def __init__(self):
        self.data = { i: 'o' * i for i in range(1, 10)}

    def add(self, msg):
        self.data[max(self.data.keys()) + 1] = msg
    
    def get(self, id):
        return self.data.get(id, None)


def create_app():
    # Create and configure the app
    app = Flask(__name__)
    # Acts like some sort of datastore.
    messages = Messages()
    ###############################################################################
    '''
    Assignment:
    
        Create two routes (Index and Message):
    
        Index:
            1.) Create an index route that responds to GET requests.
                - GET: '/'
    
            2.) Extract the optional query string parameter called: name.
                - Example query string: localhost:5000/?name=Human
    
            3.) Render the index.txt template providing the name argument to the template.
                - Provide the value of None if no name is provided in the query string. 
    
            4.) Return the rendered template.
    
        Message:
            1.) Create a message route that responds to GET and POST requests.
                - GET:  '/message/<int:id>'
                - POST: '/message/'
              
            2.) GET requests:
                - Return the message with the corresponding ID as a str.
                  - Example: curl "http://localhost:5000/message/3"
                      ooo
                - Return a 404 status if no corresponding message exists.
    
            3.) POST requests:
                - Extract the message from the posted form.
                - Pass the posted message to the messages.add method to save the message.
                - Return a 201 status.
    '''
    # Add routes below
    ###############################################################################
    @app.route('/', methods=['GET'])
    def index():
        name = request.args.get('name', None)
        return render_template('index.txt', name=name)

    @app.route('/message/<int:id>', methods=['GET'])
    def get_message(id):
        msg = messages.get(id)
        if msg is None:
            return '', 404
        return str(msg)

    @app.route('/message/', methods=['POST'])
    def post_message():
        msg = request.form.get('message')
        if msg is None:
            return 'Missing message', 400
        messages.add(msg)
        return '', 201
    # End routes.
    ###########################################################################

    return app


if __name__ == '__main__':
    # Create a server and run the app until the process is terminated.
    server = make_server('', 5000, create_app())
    server.serve_forever()
    # Test for yourself as needed:
    # python3 playground/challenge_3.py
    # 
    # In another terminal use CURL to issue HTTP requests.
    # 
    # curl "http://localhost:5000/message/" -H "Content-Type: application/x-www-form-urlencoded" -d 'message=test'