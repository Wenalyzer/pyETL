from pathlib import Path

import requests
import pandas as pd
from bs4 import BeautifulSoup

from crawler_utilities import extract_article_op_IP

# 設定儲存文章的資料夾路徑
FOLDER_PATH = Path("./ptt_articles_op_IP")
# 建立資料夾（若不存在則自動建立）
FOLDER_PATH.mkdir(parents=True, exist_ok=True)

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

cookies = {"over18": "1"}

ip_country = []
for _ in range(20):
    # 發送 GET 請求取得網頁內容
    res = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(res.text, "html.parser")

    # 取得所有文章標題區塊
    title_tag_list = soup.select('div[class="title"]')

    for tag in title_tag_list:
        # 取得標題連結標籤
        title_a_tag = tag.select_one("a")
        # 取得標題文字
        title = title_a_tag.text if title_a_tag else "No Title"
        # 取得文章網址
        article_url = "https://www.ptt.cc" + title_a_tag["href"] if title_a_tag else "No URL"

        print(f"Title: {title}")
        print(f"URL: {article_url}")
        
        # 若無法取得網址則跳過
        if "No URL" in article_url:
            print("No URL found, skipping...")
            print()
            continue

        # 擷取文章OP的IP
        result = extract_article_op_IP(article_url, headers, cookies)
        if result:
            print(result)
            print()
            ip_country.append(result)
        else:
            continue

    # 取得「上頁」按鈕，更新 url 以便爬取上一頁
    for btn_tag in soup.select('a[class="btn wide"]'):
        if "上頁" in btn_tag.text:
            url = "https://www.ptt.cc" + btn_tag["href"]
            break
    else:
        # 若找不到「上頁」按鈕則結束爬蟲
        print("No previous page found.")
        break
    print("=====================================")

columns = ['IP地址', '國家']
df = pd.DataFrame(data=ip_country, columns=columns)
df.to_csv(r'./0421/ptt_articles_op_ip/pttGossiping.csv', index=False, encoding='utf-8-sig')