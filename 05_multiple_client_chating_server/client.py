import socket
import threading

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            break

s = socket.socket()
s.connect(("127.0.0.1", 5005))

# receive thread
threading.Thread(target=receive, args=(s,), daemon=True).start()

while True:
    msg = input()
    s.send(msg.encode())