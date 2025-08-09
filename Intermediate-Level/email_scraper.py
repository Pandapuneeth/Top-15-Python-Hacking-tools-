# email_scraper.py
import requests
from bs4 import BeautifulSoup
import re

url = "https://example.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", soup.text))

print("[*] Emails found:")
for email in emails:
    print(email)
