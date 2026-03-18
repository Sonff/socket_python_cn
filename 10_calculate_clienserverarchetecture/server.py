import socket

# create socket
s = socket.socket()

# bind
s.bind(("127.0.0.1", 12345))

# listen
s.listen(1)

print("Server waiting for client...")

# accept connection
conn, addr = s.accept()
print("Connected with:", addr)

# receive data
data = conn.recv(1024).decode()

# split input
num1, op, num2 = data.split()

num1 = float(num1)
num2 = float(num2)

# perform operation
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2
else:
    result = "Invalid Operator"

# send result
conn.send(str(result).encode())

# close
conn.close()
s.close()