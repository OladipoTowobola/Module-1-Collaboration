import socket

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(5)
print('Server is listening...')

while True:
    client, addr = server.accept()
    print('Connected from', addr)
    data = client.recv(1024)
    print('Received from client:', data.decode())
    client.send("Hello, Client!".encode())
    client.sendall(data)
    client.close()
    