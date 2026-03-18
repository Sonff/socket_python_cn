import socket

# create socket
s = socket.socket()

# bind
s.bind(("127.0.0.1", 5000))

# listen
s.listen(1)
print("Server running... waiting for client")

# accept connection
c, addr = s.accept()
print("Connected:", addr)

# receive year
year = int(c.recv(1024).decode())

# check leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = "Leap Year"
else:
    result = "Not a Leap Year"

# send result
c.send(result.encode())

# close
c.close()
s.close()