import socket

# create socket
s = socket.socket()

# bind
s.bind(("127.0.0.1", 65432))

# listen
s.listen(1)

print("Server is waiting for client...")

# accept connection
conn, addr = s.accept()
print("Connected with:", addr)

# receive request
request = conn.recv(1024).decode()
print("Client request:", request)

# server name
server_name = "MyServer"

# send server name
conn.send(server_name.encode())

# close
conn.close()
s.close()