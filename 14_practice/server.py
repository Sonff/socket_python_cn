import socket
import datetime 

s=socket.socket()
s.bind("localhost", 123456)

s.listen(1)

print("server waiting...")

conn, addr=s.sccept()
now = str(datetime.datetime.now())

conn.send(now.encode())
conn.close()
s.close()
