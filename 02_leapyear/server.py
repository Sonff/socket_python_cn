import socket

s = socket.socket()
s.bind(('127.0.0.1', 5001))
s.listen(1)

print("Server running...")

conn, addr = s.accept()
print("Connected to:", addr)

year = int(conn.recv(1024).decode())

# Leap year logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = "Leap Year"
else:
    result = "Not a Leap Year"

conn.send(result.encode())

conn.close()
s.close()