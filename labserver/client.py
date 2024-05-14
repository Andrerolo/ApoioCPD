import socket

 

 

class JSONRPCClient:

    """The JSON-RPC client."""

 

    def __init__(self, host, port):

        self.sock = socket.socket()

        self.sock.connect((host, port))

 

    def send(self, msg):

        """Sends a message to the server."""

        self.sock.sendall(msg.encode())

        return self.sock.recv(1024).decode()

 

 

if __name__ == "__main__":

 

    # Test the JSONRPCClient class

    client = JSONRPCClient('127.0.0.1', 8000)

    res = client.send('Hello World')

    print(res)