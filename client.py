import socket 
client = socket.socket()
client.connect(('localhost', 9999))
client.send('Hello Server'.encode())
response = client.recv(1024).decode()
print('Response from server:', response)    
client.close()