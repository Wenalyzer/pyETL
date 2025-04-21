from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

url = 'https://www.ptt.cc/bbs/index.html'

# input()
driver.get(url)
# input()
driver.find_element(by=By.CLASS_NAME, value='board').click()
# input()
driver.find_element(by=By.CLASS_NAME, value='btn-big').click()

cookies = driver.get_cookies()


# input()
driver.quit()

# cookie is a list of dict
# print(type(cookies[0]))

ss = requests.sessions.Session()

# 設定cookies
for cookie in cookies:
    print(f"Cookie name: {cookie['name']}\nCookie value: {cookie['value']}\n")
    ss.cookies.set(cookie['name'], cookie['value'])

print(type(ss.cookies))

# res = ss.get('https://www.ptt.cc/bbs/Gossiping/index.html')
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
