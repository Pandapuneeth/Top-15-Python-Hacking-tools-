# advanced_sniffer.py
from scapy.all import sniff, IP, TCP, UDP

def packet_callback(pkt):
    if IP in pkt:
        proto = "TCP" if pkt.haslayer(TCP) else "UDP" if pkt.haslayer(UDP) else "Other"
        print(f"{pkt[IP].src} --> {pkt[IP].dst} | Proto: {proto} | Len: {len(pkt)}")

print("[*] Sniffing started...")
sniff(prn=packet_callback, count=20)
