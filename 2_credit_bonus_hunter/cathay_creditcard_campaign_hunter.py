from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime

PROMO_URL = 'https://www.cathaybk.com.tw/promotion/'
TARGET_CAMPAIGN = "PChome"
TARGET_TIME = datetime.datetime(2025, 5, 24, 16, 0, 0)
WAIT_SECONDS = 1

def setup_driver():
    """啟動並回傳 ChromeDriver 物件"""
    print("啟動 ChromeDriver 中...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    print("已啟動 ChromeDriver")
    return driver

def wait_until(target_time):
    """等待到指定時間"""
    print(f"等待到 {target_time} ...")
    while datetime.datetime.now() < target_time:
        time.sleep(0.1)

def find_and_click_campaign(driver, wait, campaign_name):
    """不斷刷新直到找到指定活動並點擊登錄按鈕"""
    print(f"開始尋找活動：{campaign_name}")
    while True:
        try:
            driver.refresh()
        except Exception:
            print("刷新超時，繼續下一輪")
        try:
            row = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//a[contains(@class, 'campaign-name') and contains(text(), '{campaign_name}')]/ancestor::div[contains(@class, 'tr')]")
                )
            )
            login_btn = row.find_element(By.XPATH, ".//a[contains(@class, 'btn-sign')]//span[text()='登錄']")
            login_btn.click()
            print("已點擊活動的登錄按鈕")
            return True
        except Exception as e:
            print("尚未找到活動，繼續刷新...", e)
            time.sleep(0.1)  # 避免過度頻繁刷新

def main():
    driver = setup_driver()
    driver.get(PROMO_URL)
    input("請手動登入後按 Enter 繼續...")

    driver.set_page_load_timeout(WAIT_SECONDS)
    wait = WebDriverWait(driver, WAIT_SECONDS)

    wait_until(TARGET_TIME)
    find_and_click_campaign(driver, wait, TARGET_CAMPAIGN)

    input("按 Enter 結束並關閉瀏覽器...")
    driver.quit()

if __name__ == "__main__":
    main()