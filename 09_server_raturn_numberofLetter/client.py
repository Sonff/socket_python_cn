import socket

# create socket
c = socket.socket()

# connect
c.connect(("127.0.0.1", 1234))

# input message
msg = input("Enter message: ")

# send
c.send(msg.encode())

# receive result
count = c.recv(1024).decode()

print("Number of letters:", count)

# close
c.close()