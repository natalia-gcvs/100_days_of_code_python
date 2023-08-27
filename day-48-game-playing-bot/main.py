from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
from price_checker import PriceChecker


timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes


option = ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
price_checker = PriceChecker()

while True:
    driver.find_element(By.XPATH, '//*[@id="cookie"]').click()
    if time.time() > timeout:
        data_prices = price_checker.compare_prices(driver=driver).click()
        timeout = time.time() + 5

    if time.time() > five_min:
        cookies_second = driver.find_element(By.XPATH, '//*[@id="cps"]').get_attribute("textContent")
        print(cookies_second)
        break





