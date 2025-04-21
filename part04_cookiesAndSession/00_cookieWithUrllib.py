from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Cookie': 'over18=1',
}

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

print(res.read().decode('utf-8'))
