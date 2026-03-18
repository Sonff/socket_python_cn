import socket

def sum_digits(n):
    return sum(int(d) for d in n if d.isdigit())

# create socket
s = socket.socket()

# bind
s.bind(("127.0.0.1", 5006))

# listen
s.listen(1)

print("Server running... waiting for client")

# accept connection
c, addr = s.accept()
print("Connected:", addr)

# receive number
num = c.recv(1024).decode()

# calculate sum
result = str(sum_digits(num))

# send result
c.send(("Sum of digits = " + result).encode())

# close
c.close()
s.close()