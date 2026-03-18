import socket

# create socket
s = socket.socket()

# connect to server
s.connect(("127.0.0.1", 5000))

# input from user
year = input("Enter your birth year: ")

# send to server
s.send(year.encode())

# receive result
result = s.recv(1024).decode()

# display result
print("Result:", result)

# close
s.close()