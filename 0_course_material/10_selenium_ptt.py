from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests

import time

url = "https://www.ptt.cc/bbs/index.html"

# 不產生視窗
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1080,720")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get(url)

# gossiping_xpath = '//*[@id="main-container"]/div[2]/div[1]/a/div[1]'
# driver.find_element(By.XPATH, value=gossiping_xpath).click()

# baseball_xpath = '//*[@id="main-container"]/div[2]/div[2]/a/div[1]'

title = "Gossiping"
driver.find_element(By.PARTIAL_LINK_TEXT, value=title).click()

button_xpath = "/html/body/div[2]/form/div[1]/button"
driver.find_element(By.XPATH, value=button_xpath).click()

print()
print(driver.get_cookies())

cookies = {
    cookie_set['name']: cookie_set['value']
    for cookie_set in driver.get_cookies()
}

print()
print(cookies)

driver.quit()

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers, cookies=cookies)

print(res.text)