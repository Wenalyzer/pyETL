from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

url = 'https://www.cathaybk.com.tw/promotion/'

print("啟動 ChromeDriver 中...")
driver = webdriver.Chrome()
print("已啟動 ChromeDriver")
driver.get(url)
input("先手動登入")

driver.set_page_load_timeout(1) # 設定頁面載入超時為1秒，避免refresh卡住
wait = WebDriverWait(driver, 1) # 設定顯式等待，每次最多等1秒

# 等待到指定時間
target_time = datetime.datetime(2025, 4, 24, 16, 0, 0)
while datetime.datetime.now() < target_time:
    time.sleep(0.1)

# 不斷刷新直到出現活動
found = False
while not found:
    try:
        driver.refresh()
    except Exception as e:
        print("刷新超時，繼續下一輪")
    try:
        # 找到包含活動名稱的row
        row = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'campaign-name') and contains(text(), 'PChome')]/ancestor::div[contains(@class, 'tr')]")
            )
        )
        # 找到該row內的「登錄」按鈕
        login_btn = row.find_element(By.XPATH, ".//a[contains(@class, 'btn-sign')]//span[text()='登錄']")
        login_btn.click()
        found = True
        print("已點擊活動的登錄按鈕")
    except Exception as e:
        print("exception:", e)

input("按Enter結束")
driver.quit()