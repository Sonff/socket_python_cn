import socket

s = socket.socket()

s.connect(('127.0.0.1', 5000))

data = s.recv(1024).decode()

print("Current Date and Time:", data)

s.close()