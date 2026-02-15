import socket
server = socket.socket()
server.bind(('localhost', 9999))
server.listen(5)    
print('Server is listening...')
while True:
    client, addr = server.accept()
    print('Connected from', {addr}")
    data = client.recv(1024)
    print('Received from client:', data.encode())
    conn.send("Hello, Client!".encode())  # Send a welcome message to the client
    client.sendall(data)  # Echo back the received data
    conn.close()
    