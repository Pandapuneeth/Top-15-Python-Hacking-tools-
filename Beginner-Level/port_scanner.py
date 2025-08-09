# threaded_port_scanner.py
import socket
import threading

target = input("Enter IP to scan: ")
print(f"Scanning {target}...")

open_ports = []

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
        sock.close()
    except:
        pass

threads = []

for port in range(1, 1025):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

if not open_ports:
    print("[-] No open ports found.")
