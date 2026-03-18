import socket

# create socket
c = socket.socket()

# connect
c.connect(("127.0.0.1", 12345))

# input
num1 = input("Enter first number: ")
op = input("Enter operator (+ - * /): ")
num2 = input("Enter second number: ")

# create message
msg = num1 + " " + op + " " + num2

# send
c.send(msg.encode())

# receive result
result = c.recv(1024).decode()

print("Result from server:", result)

# close
c.close()