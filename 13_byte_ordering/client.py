import socket

# create socket
c = socket.socket()

# connect
c.connect(("127.0.0.1", 12345))

# send request
c.send("ENDIAN".encode())

# receive result
result = c.recv(1024).decode()

print("Server Byte Ordering:", result)

# close
c.close()