import socket

 

 

class JSONRPCServer:

    """The JSON-RPC server."""

 

    def __init__(self, host, port):

        self.host = host

        self.port = port

 

    def start(self):

        """Starts the server."""

        sock = socket.socket()

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sock.bind((self.host, self.port))

        sock.listen(1)

        print('Listening on port %s ...' % self.port)

 

        while True:

            # Accept client

            conn, _ = sock.accept()

 

            # Receive message

            msg = conn.recv(1024).decode()

            print('Received:', msg)

 

            # Send response

            res = msg

            conn.send(res.encode())

 

            # Close client connection

            conn.close()

 

 

if __name__ == "__main__":

 

    # Test the JSONRPCServer class

    server = JSONRPCServer('0.0.0.0', 8000)

    server.start()

 

 