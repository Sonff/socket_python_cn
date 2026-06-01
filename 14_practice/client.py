import socket

c = socket.socket()
c.connect(("localhost",123456))
data= c.recv(1024).decode()
print(data)
c.close()
