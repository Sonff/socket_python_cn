import socket

# create socket
c = socket.socket()

# connect
c.connect(("127.0.0.1", 65432))

# send request
c.send("Send your IP address".encode())

# receive IP
server_ip = c.recv(1024).decode()

print("Server IP Address:", server_ip)

# close
c.close()