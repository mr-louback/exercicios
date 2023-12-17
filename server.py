import socket

HOST = "localhost"
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Waiting...") 
conn, ender = s.accept()
print("Connected to", ender)
while True:
    data = conn.recv(1024)
    if not data:
        print("Closing connection")
        conn.close()
        break
    conn.sendall(data)
