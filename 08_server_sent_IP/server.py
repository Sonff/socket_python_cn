import socket

# create socket
s = socket.socket()

# bind (0.0.0.0 = all interfaces)
s.bind(("0.0.0.0", 65432))

# listen
s.listen(1)

print("Server waiting for client...")

# accept connection
conn, addr = s.accept()
print("Connected with:", addr)

# receive request
msg = conn.recv(1024).decode()
print("Client says:", msg)

# get server IP
server_ip = socket.gethostbyname(socket.gethostname())

# send IP to client
conn.send(server_ip.encode())

# close
conn.close()
s.close()