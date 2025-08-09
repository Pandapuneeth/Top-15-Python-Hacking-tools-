import ipaddress
import subprocess

def ping(ip):
    try:
        output = subprocess.check_output(['ping', '-n', '1', '-w', '100', str(ip)], stderr=subprocess.DEVNULL)
        return "TTL=" in output.decode()
    except:
        return False

def scan_network(network_cidr):
    network = ipaddress.ip_network(network_cidr, strict=False)
    print(f"Scanning network: {network}")
    
    found = False
    for ip in network.hosts():
        print(f"[*] Pinging {ip}...")
        if ping(ip):
            print(f"[+] Active device found: {ip}")
            found = True

    if not found:
        print("[!] No active devices found in this range.")

if __name__ == "__main__":
    scan_network("192.168.1.0/28")
