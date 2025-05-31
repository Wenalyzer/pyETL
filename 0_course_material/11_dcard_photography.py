from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
import random
import time

# 隨機 User-Agent
ua = UserAgent()
user_agent = ua.random
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-agent={user_agent}")

# 移除 headless 模式，讓瀏覽器有視窗
# chrome_options.add_argument("--headless")  # 註解掉這行

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 隱藏 webdriver 屬性
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

def human_sleep(a=0.5, b=1.5):
    time.sleep(random.uniform(a, b))

url = 'https://www.dcard.tw/f'
driver.get(url)
human_sleep(1, 2)

search_form = '//*[@id="__next"]/div[1]/div/div[1]/div/div/form/input'
search_input = driver.find_element(By.XPATH, value=search_form)

actions = ActionChains(driver)

# 模擬滑鼠緩慢移動到搜尋欄位
location = search_input.location
size = search_input.size
center_x = location['x'] + size['width'] // 2
center_y = location['y'] + size['height'] // 2
driver.execute_script(f"window.scrollTo({center_x}, {center_y})")
human_sleep(0.5, 1.2)
actions.move_to_element(search_input).perform()
human_sleep(0.3, 0.8)
actions.click(search_input).perform()
human_sleep(0.3, 0.8)
for c in '攝影':
    actions.send_keys(c).perform()
    human_sleep(0.2, 0.5)

human_sleep(1, 2)

search_button = '//*[@id="__next"]/div[1]/div/div[1]/div/div/form/button[2]'
search_btn = driver.find_element(By.XPATH, value=search_button)

# 滑鼠移動到按鈕再點擊
actions.move_to_element(search_btn).perform()
human_sleep(0.3, 0.8)
actions.click(search_btn).perform()

human_sleep(5, 8)
driver.quit()