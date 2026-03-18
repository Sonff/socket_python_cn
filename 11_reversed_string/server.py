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

# reverse string
reversed_string = data[::-1]

# send result
conn.send(reversed_string.encode())

# close
conn.close()
s.close()