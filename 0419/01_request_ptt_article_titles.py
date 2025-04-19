import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

cookies = {"over18": "1"}

res = requests.get(url, headers=headers, cookies=cookies)

# a string of HTML
# print(res.text) 

soup = BeautifulSoup(res.text, "html.parser")
# print(type(soup))
# print(soup.prettify())

# title_tag = soup.select_one("div.title")
title_tag = soup.select_one('div[class="title"]')

# title_tag = soup.find("div", {"class": "title"})
# title_tag = soup.find("div", class_="title")
# print(type(title_tag))

title_tag_list = soup.select('div[class="title"]')
# title_tag_list = soup.find_all("div", class_="title")
# print(title_tag_list)

for tag in title_tag_list:
    title_a_tag = tag.select_one("a")
    title = title_a_tag.text if title_a_tag else "No Title"
    article_url = "https://www.ptt.cc" + title_a_tag["href"] if title_a_tag else "No URL"

    # print(f"Source HTML: {title_a_tag}")
    print(f"Title: {title}")
    print(f"URL: {article_url}")
    print("----------------------------------")