from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

option = ChromeOptions()
option.add_argument("start-maximized")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=option)

# # wikipedia challenge
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# no_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').get_attribute("textContent")
# print(no_articles)
#
# no_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').click()
#
# view_source = driver.find_element(By.LINK_TEXT, "View source").click()
#
# search_bar = driver.find_element(By.NAME, "search").send_keys("Python")

#the app brewery challenge

driver.get("https://www.appbrewery.co/p/newsletter")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)


subscribe_button = driver.find_element(By.XPATH, '//*[@id="blocks"]/section[2]/div/a').click()
time.sleep(10)
name_input_box = driver.find_element(By.NAME, "name").send_keys("Natalia Miranda")
time.sleep(10)
email_input_box_click = driver.find_element(By.NAME, "email").click()
time.sleep(10)
email_input_box_type_in = driver.find_element(By.NAME, "email").send_keys("natalia.gcvs@gmail.com")
time.sleep(10)
agree_check_box = driver.find_element(By.NAME, "gdpr").click()
time.sleep(10)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

time.sleep(30)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))

send_details = driver.find_element(By.LINK_TEXT, 'Subscribe to list').click()


time.sleep(20)







