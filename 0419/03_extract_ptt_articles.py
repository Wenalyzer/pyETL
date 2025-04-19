from pathlib import Path

import requests
from bs4 import BeautifulSoup

from crawler_utilities import extract_article_content
from crawler_utilities import replace_illegal_chars

# 設定儲存文章的資料夾路徑
FOLDER_PATH = Path("./test/ptt_articles")
# 建立資料夾（若不存在則自動建立）
FOLDER_PATH.mkdir(parents=True, exist_ok=True)

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

cookies = {"over18": "1"}

for _ in range(2):
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

        # print(f"Source HTML: {title_a_tag}")
        print(f"Title: {title}")
        # print(f"URL: {article_url}")
        print("----------------------------------")
        # 若無法取得網址則跳過
        if "No URL" in article_url:
            continue

        # 擷取文章主文內容
        article_content = extract_article_content(article_url)
        # 將標題轉為合法檔名
        acrticle_file_name = replace_illegal_chars(f"{title}.txt")
        # 組合完整檔案路徑
        artcicle_file_path = FOLDER_PATH / acrticle_file_name
        # 將文章內容寫入檔案
        with open(artcicle_file_path, "w", encoding="utf-8") as f:
            f.write(article_content)
        print(f"Article content saved to {artcicle_file_path}")
        print("----------------------------------")
    
    # url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]

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