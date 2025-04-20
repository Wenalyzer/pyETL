import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

url = 'http://httpbin.org/post'

data = {'key1': 'value1', 'key2': 'value2'}
res = requests.post(url, data=data, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())
