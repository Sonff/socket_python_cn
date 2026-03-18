import socket

# create socket
c = socket.socket()

# connect to server
c.connect(("127.0.0.1", 65432))

# send request
c.send("Send your name".encode())

# receive server name
name = c.recv(1024).decode()

print("Server Name:", name)

# close
c.close()