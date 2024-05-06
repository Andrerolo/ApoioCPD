import socket

server_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 8000)) #127.0.0.1 => vai escutar para localhost || 0.0.0.0 => geral ou internet 
server_socket.listen(1)
print('listening on port 8000')

while True:
    #wait for client
    client_conn, client_addr = server_socket.accept()

    while True:
        #ler msg
        msg = client_conn.recv(1024).decode()
        print(msg)

        #return answer
        res = str(eval(msg))
        client_conn.sendall(msg.encode())

        if msg == 'exit':
            break


#close sockets
client_conn.close()
server_socket.close()