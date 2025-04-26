import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

import rookiepy
cookies = rookiepy.edge(["ptt.cc"])
for cookie in cookies:
    print(f"Cookie Domain: {cookie['domain']},\nCookie: {cookie['value']}")

r = requests.get(url, cookies=cookies[0]['value'])

print(r.status_code)
print(r.text)