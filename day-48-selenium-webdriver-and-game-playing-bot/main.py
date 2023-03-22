from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:/Users/natal/Documents/Development/chromedriver"
options = ChromeOptions()
driver = webdriver.Chrome(options=options)


# driver.get("https://www.amazon.co.uk/Uten-Automatic-Multifunctional-Tabletop-Temperature/dp/B08MQ2H27R/ref=sr_1_6?"
#            "crid=MGM06NDG8EKD&keywords=air+fryers&qid=1678826264&sprefix=air%2Caps%2C310&sr=8-6")
#
# driver.find_element(By.ID, "sp-cc-accept").click()
# continue_button = driver.find_element(By.CLASS_NAME, "a-button-inner")
#
#
# price = driver.find_element(By.CLASS_NAME, "a-offscreen").get_attribute("textContent")
#
# print(price)
#
# driver.close()

driver.get("https://www.python.org")

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")


events_dates = {index: {dates[index].get_attribute("textContent"):
                        events[index].get_attribute("textContent")}
                for index in range(len(dates))}

print(events_dates)


