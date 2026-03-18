import socket

# create socket
s = socket.socket()

# bind
s.bind(("127.0.0.1", 12345))

# listen
s.listen(1)

print("Server waiting for client...")

# accept connection
conn, addr = s.accept()
print("Connected to:", addr)

# receive string
data = conn.recv(1024).decode()

# count characters
count = len(data)

# send result
conn.send(str(count).encode())

# close
conn.close()
s.close()