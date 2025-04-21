from selenium import webdriver                # 匯入 selenium 的 webdriver 模組
from selenium.webdriver.common.by import By   # 匯入 By，用於指定查找元素的方法

driver = webdriver.Chrome()                   # 啟動 Chrome 瀏覽器

driver.get('https://selenium.dev/documentation')  # 開啟指定網址
print(driver.title)
assert 'Selenium' in driver.title                 # 確認網頁標題包含 'Selenium'

elem = driver.find_element(By.ID, 'm-documentationwebdriver')  # 以 ID 找到指定元素
elem.click()                                       # 點擊該元素
print(driver.title)
assert 'WebDriver' in driver.title                 # 確認網頁標題包含 'WebDriver'

driver.quit()                                      # 關閉瀏覽器