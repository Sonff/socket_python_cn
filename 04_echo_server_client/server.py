import socket

# create socket
s = socket.socket()

# bind
s.bind(("127.0.0.1", 5000))

# listen
s.listen(1)

print("Echo Server running... waiting for client")

# accept connection
c, addr = s.accept()
print("Connected:", addr)

# receive message
msg = c.recv(1024).decode()

# send back (echo)
c.send(("Echo: " + msg).encode())

# close
c.close()
s.close()