from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

FACE_EMAIL = ""
FACE_PASSWORD = ""

option = ChromeOptions()
driver = webdriver.Chrome(options=option)

driver.get("https://tinder.com/app/recs")


# accept terms
time.sleep(3)
accept = driver.find_element(By.XPATH, '//*[@id="q-586956664"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]').click()


# tinder login
time.sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="q-586956664"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]').click()

#login to tinder using facebook
time.sleep(2)
login_with_face = driver.find_element(By.CSS_SELECTOR, '#q1979629556 > main > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div:nth-child(3) > span > div:nth-child(2) > button').click()

# switch to facebook window login
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# login to facebook
time.sleep(2)
face_username = driver.find_element(By.XPATH, '//*[@id="email"]')
face_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
face_username.send_keys("FACE_EMAIL")
face_password.send_keys('FACE_PASSWORD')
face_password.send_keys(Keys.ENTER)

#switch back to tinder window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()





