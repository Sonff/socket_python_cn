import socket
import threading

clients = []

def handle(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                break
            # send message to all clients
            for c in clients:
                if c != client:
                    c.send(msg.encode())
        except:
            break

    clients.remove(client)
    client.close()

# create socket
s = socket.socket()
s.bind(("127.0.0.1", 5005))
s.listen(5)

print("Server running... waiting for clients")

while True:
    client, addr = s.accept()
    print("Client connected:", addr)
    
    clients.append(client)

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()