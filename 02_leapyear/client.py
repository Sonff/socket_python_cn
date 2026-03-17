import socket

s = socket.socket()

s.connect(('127.0.0.1', 5001))

year = input("Enter year: ")

s.send(year.encode())

result = s.recv(1024).decode()

print("Result:", result)

s.close()