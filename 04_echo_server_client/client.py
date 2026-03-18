import socket

# create socket
s = socket.socket()

# connect to server
s.connect(("127.0.0.1", 5000))

# input message
msg = input("Enter message: ")

# send message
s.send(msg.encode())

# receive echo
print("From Server:", s.recv(1024).decode())

# close
s.close()