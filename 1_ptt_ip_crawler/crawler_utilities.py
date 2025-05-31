import requests
from bs4 import BeautifulSoup
import re

def extract_article_content(article_url: str, header: dict, cookie: dict) -> str:
    """
    Extracts the content of an article from the given URL.
    """
    res = requests.get(article_url, headers=header, cookies=cookie)
    soup = BeautifulSoup(res.text, "html.parser")
    article_content_tag = soup.select_one('div[id="main-content"]')

    # Remove unwanted tags
    for tag in ["div", "span"]:
        for element in article_content_tag.select(tag):
            element.extract()
    return article_content_tag.text.strip()

def extract_article_op_IP(article_url: str, header: dict, cookie: dict) -> list[str]:
    """
    Extracts the OP IP and country from the article page.
    """
    res = requests.get(article_url, headers=header, cookies=cookie)
    soup = BeautifulSoup(res.text, "html.parser")
    article_op_IP_tags = soup.select('span[class="f2"]')

    for tag in article_op_IP_tags:
        match = re.search(r'來自:\s*([\d\.]+)\s*\(([^)]+)\)', tag.text)
        if match:
            ip = match.group(1)
            country = match.group(2)   
            return [ip, country]
    
    print("No match found")

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