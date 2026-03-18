import socket

# create socket
s = socket.socket()

# bind
s.bind(("127.0.0.1", 1234))

# listen
s.listen(1)

print("Server waiting...")

# accept connection
conn, addr = s.accept()

# receive message
msg = conn.recv(1024).decode()

# count letters
count = len(msg)

# send result
conn.send(str(count).encode())

# close
conn.close()
s.close()