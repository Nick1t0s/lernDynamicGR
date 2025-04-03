import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8080))
for i in range(100000):
    sock.send(b"Test\n")
    # time.sleep(1)
sock.close()