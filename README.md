# 🛡️ Cybersecurity Toolkit

A collection of hands-on cybersecurity tools and simulations built with Python.  
This repository is designed for **educational and ethical hacking** purposes — ideal for learning, training, and showcasing skills.

---

## 📂 Project List

### **Beginner Level**
1. **Port Scanner** – Scan open ports on a target host using sockets.
2. **Basic Packet Sniffer** – Capture network packets (requires Scapy + WinPcap/libpcap).
3. **Keylogger (Educational)** – Record keystrokes locally for demonstration purposes.
4. **Password Strength Checker** – Check password security against common patterns.
5. **Hash Cracker (Dictionary Attack)** – Attempt to crack hashes using a wordlist.

### **Intermediate Level**
6. **Directory Brute Forcer** – Discover hidden directories on a web server.
7. **Subdomain Scanner** – Enumerate subdomains from a given domain.
8. **ARP Spoof Detector** – Detect suspicious ARP packets in the network.
9. **Simple Vulnerability Scanner** – Scan for common web vulnerabilities.
10. **Basic Firewall** – Filter packets based on custom rules.

### **Advanced Level**
11. **Ransomware Simulation** – File encryption/decryption demo using the `cryptography` library.
12. **Reverse Shell** – Client-server architecture for remote command execution.
13. **Malware Analysis Tool** – Analyze file properties using `pefile` & `hashlib`.
14. **Custom Firewall** – Monitor & filter traffic with advanced Scapy rules.
15. **Advanced Packet Sniffer** – Packet capture with detailed analysis.

---

## 🚀 Installation
```bash
# Clone the repo
git clone https://github.com/yourusername/cybersecurity-toolkit.git
cd cybersecurity-toolkit

# Create a virtual environment
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt


⚙️ Usage
Each tool is in its own Python file. Run them individually:

python port_scanner.py
python ransomware_sim.py


🛑 Disclaimer
This project is for educational purposes only.
Do not use these tools on networks, systems, or devices without explicit permission.
The author assumes no responsibility for misuse.


📜 License
MIT License – free to use, modify, and distribute for educational purposes.


🌟 Future Plans
Combine all tools into a single Tkinter/Streamlit GUI.

Add reporting & logging features.

Expand AI-based threat detection models.