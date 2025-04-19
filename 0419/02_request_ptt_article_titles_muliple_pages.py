import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

cookies = {"over18": "1"}

for _ in range(3):
    res = requests.get(url, headers=headers, cookies=cookies)

    soup = BeautifulSoup(res.text, "html.parser")

    title_tag_list = soup.select('div[class="title"]')

    for tag in title_tag_list:
        title_a_tag = tag.select_one("a")
        title = title_a_tag.text if title_a_tag else "No Title"
        article_url = "https://www.ptt.cc" + title_a_tag["href"] if title_a_tag else "No URL"

        # print(f"Source HTML: {title_a_tag}")
        print(f"Title: {title}")
        print(f"URL: {article_url}")
        print("----------------------------------")

    # Update URL
    # url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]

    for btn_tag in soup.select('a[class="btn wide"]'):
        if "上頁" in btn_tag.text:
            url = "https://www.ptt.cc" + btn_tag["href"]
            break
    else:
        print("No previous page found.")
        break
    print("=====================================")