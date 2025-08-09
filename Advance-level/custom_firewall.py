# custom_firewall.py
from scapy.all import sniff, IP

BLOCKED_IPS = ["192.168.1.5"]

def packet_filter(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        if src in BLOCKED_IPS:
            print(f"[!] Blocked packet from {src}")
        else:
            print(f"[+] Allowed: {src}")

sniff(prn=packet_filter, store=0)
