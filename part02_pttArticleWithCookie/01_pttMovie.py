import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
url = 'https://www.ptt.cc/bbs/movie/index.html'

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.prettify())

article_title_html = soup.select('div[class="title"]')
# print(article_title_html)

for each_article in article_title_html:
    print(each_article.a.text)
    print('https://www.ptt.cc' + each_article.a['href'])
    print()
