import socket
import threading


class MessageServer:

    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.msgs = []


    def serve(self):
        ''' A basic TCP/IP listener. 

            Listens on the supplied host/port for binary data.
        '''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            sock.listen(1)
            while True:
                conn, addr = sock.accept()
                with conn:
                    while (mess := conn.recv(1024)):
                        # Store all the messages.
                        self.msgs.append(mess)
                        # Echo the message back to the client.
                        conn.sendall(mess)


    def serve_forever(self, **kwargs):
        ''' Runs the message_server function in a background thread. 
            Must be running before the client can be used.
        '''
        server = threading.Thread(target=self.serve, kwargs=kwargs, name='network_server', daemon=True)
        server.start()


    def search(self, fn: callable):
        ''' 
            Args:
                fn  | A callable that accepts a bytes object and returns a boolean.
            
            Returns:
                A list of messages that return True when passed to the callable.
        '''
        return [msg for msg in self.msgs if fn(msg)]
    

    def unredacted(self):
        ''' Returns:
                A list of messages that are not redacted in the order they were received.

            >>> server = MessageServer()
            >>> server.msgs = [b'TOP SECRET: *', b'Hey!', b'Sup.', b'TOP SECRET: **']
            >>> server.unredacted()
            [b'Hey!', b'Sup.']
        '''
        


def redact():
    ''' A decorator used to redact messages sent via the send_message method of the  MessageClient. 

        Messages are expected to be bytes objects. NOT str objects.
    '''



class MessageClient:
    ''' 
        >>> port = 1337
        >>> server = MessageServer(port=port)
        >>> server.serve_forever()
        
        Wait a second for the thread to get the server running.
        >>> import time; time.sleep(1.0)

        >>> with MessageClient(port=port) as client:
        ...     messages = [
        ...        b'TOP SECRET: Aliens are invading!',
        ...        b'Hey!',
        ...        b'Sup.',
        ...        b'TOP SECRET: The universe is going to collapse.'
        ...     ]
        ...     for message in messages:
        ...         print(client.send_message(message))
        b'TOP SECRET: ********************'
        b'Hey!'
        b'Sup.'
        b'TOP SECRET: **********************************'
    '''

    def __init__(self, host='127.0.0.1', port=5000):
        self.connection = None
        self.host = host
        self.port = port

    
    def send_message(self, message) -> bytes:
        self.connection.sendall(message)
        return self.connection.recv(1024)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL, verbose=True)
   
