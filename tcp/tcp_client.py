import socket
from random import choice
from string import ascii_letters

req = ''.join(choice(ascii_letters) for i in range(1024))
print("Request: ", req)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 2222))

sock.send(req.encode('utf-8'))
rsp = sock.recv(1024)
print("Response: ", rsp.decode('utf-8'))

sock.close()
