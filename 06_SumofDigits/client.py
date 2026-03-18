import socket

# create socket
s = socket.socket()

# connect
s.connect(("127.0.0.1", 5006))

# input
n = input("Enter a number: ")

# send
s.send(n.encode())

# receive
print(s.recv(1024).decode())

# close
s.close()