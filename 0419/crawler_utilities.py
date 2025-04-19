import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

COOKIES = {"over18": "1"}

def extract_article_content(article_url: str) -> str:
    """
    Extracts the content of an article from the given URL.
    """
    res = requests.get(article_url, headers=HEADERS, cookies=COOKIES)
    soup = BeautifulSoup(res.text, "html.parser")
    article_content_tag = soup.select_one('div[id="main-content"]')
    # article_content_tag.select_one('div[class="article-metaline"]').extract()

    for tag in ["div", "span"]:
        for element in article_content_tag.select(tag):
            element.extract()
    return article_content_tag.text.strip()
    # print(article_content_tag)

def replace_illegal_chars(file_name: str) -> str:
    """
    Replaces illegal characters in a string with underscores.
    """
    illegal_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']

    safe_name = file_name
    for char in illegal_chars:
        safe_name = safe_name.replace(char, "_")
    
    safe_name = safe_name.strip(" .")

    return safe_name

if __name__ == "__main__":
    # Example usage
    url = "https://www.ptt.cc/bbs/Gossiping/M.1745032135.A.E06.html"
    print(extract_article_content(url))
    # Output: Article content as a string