import json
from pprint import pprint

import requests

url = "https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6672919"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers)

# pprint(json.loads(res.text))
# print(type(res.text)) -> str

article_list = json.loads(res.text)['data']['newsList']
# print(len(article_list))

for article in article_list:
    arcticle_title = article['postTitle']
    article_url = article['postUrl']

    print(f"Title: {arcticle_title}")
    print(f"URL: {article_url}")