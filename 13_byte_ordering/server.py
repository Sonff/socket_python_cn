import socket
import sys

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

# receive request
request = conn.recv(1024).decode()

# check endian
if request == "ENDIAN":
    if sys.byteorder == "little":
        reply = "Little Endian"
    else:
        reply = "Big Endian"
else:
    reply = "Invalid Request"

# send reply
conn.send(reply.encode())

# close
conn.close()
s.close()