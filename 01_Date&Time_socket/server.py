import socket
import datetime

s = socket.socket()

s.bind(('127.0.0.1', 5000))
s.listen(1)

print("Server running... waiting for client")

conn, addr = s.accept()
print("Connected to:", addr)

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn.send(now.encode())

conn.close()
s.close()