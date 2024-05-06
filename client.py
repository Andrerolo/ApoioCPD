import socket

#create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server
client_socket.connect(('127.0.0.1', 8000))

while True:
    #send msg
    msg = input("> ")
    client_socket.sendall(msg.encode())
    #client_socket.sendall(b'Hello world')

    #get answer
    res = client_socket.recv(1024).decode()
    print(res)

    if msg == 'exit':
        break




client_socket.close()