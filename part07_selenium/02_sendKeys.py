from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  # 啟動 Chrome 瀏覽器

# Google 帳號登入頁面（YouTube）
url = 'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3D%252F&hl=zh-TW&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

driver.get(url)              # 開啟登入頁面
driver.implicitly_wait(20)   # 設定隱式等待 20 秒

# 輸入帳號
driver.find_element(By.ID, 'identifierId').send_keys('aegis12321@gmail.com')
time.sleep(3)
# 點擊「下一步」
driver.find_element(By.ID, 'identifierNext').click()
time.sleep(3)
# 重新整理頁面
driver.refresh()
# 再次輸入帳號
driver.find_element(By.ID, 'identifierId').send_keys('aegis12321@gmail.com')
time.sleep(3)
# 再次點擊「下一步」
driver.find_element(By.ID, 'identifierNext').click()

# 讀取密碼檔案
with open('./passwd', 'r', encoding='utf-8') as f:
    passwd = f.read()
# 輸入密碼
driver.find_element(By.CLASS_NAME, 'whsOnd').send_keys(passwd)
# 點擊「下一步」登入
driver.find_element(By.ID, 'passwordNext').click()
time.sleep(15)  # 等待登入完成

# 取得 cookies
cookie_list = driver.get_cookies()
driver.quit()   # 關閉瀏覽器