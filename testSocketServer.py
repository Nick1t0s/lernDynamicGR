import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen(5)
col = 0
conn, addr = sock.accept()
x = True

while True:
    while x:
        x = conn.recv(1024)
        print(x.decode('utf-8'))