import socket

# create socket
c = socket.socket()

# connect
c.connect(("127.0.0.1", 12345))

# input
msg = input("Enter a string: ")

# send
c.send(msg.encode())

# receive result
result = c.recv(1024).decode()

print("Number of characters:", result)

# close
c.close()