from selenium import webdriver
import time

# 建立 Chrome 瀏覽器 WebDriver 物件
driver = webdriver.Chrome()
url = 'https://www.dcard.tw/f'

# 開啟 Dcard 看板頁面
driver.get(url)
# 等待 5 秒，讓網頁載入
time.sleep(5)

# 定義 JavaScript 指令：將頁面捲動到底部
js = "var q=document.documentElement.scrollTop=10000"
# 定義 JavaScript 指令：將頁面捲動到頂部
js2 = "var q=document.documentElement.scrollTop=0"

# 執行捲動到底部
driver.execute_script(js)
time.sleep(5)
# 執行捲動到頂部
driver.execute_script(js2)
time.sleep(5)
# 再次捲動到底部
driver.execute_script(js)
time.sleep(5)
# 再次捲動到頂部
driver.execute_script(js2)
time.sleep(5)
# 再次捲動到底部
driver.execute_script(js)
time.sleep(5)
# 再次捲動到頂部
driver.execute_script(js2)
time.sleep(5)
# 最後再捲動到底部
driver.execute_script(js)

driver.quit()