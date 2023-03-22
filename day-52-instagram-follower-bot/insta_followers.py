import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class InstaFollowers:
    def __init__(self):
        self.driver = webdriver.Chrome(options=ChromeOptions())

    def login(self, username_, password_):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(username_)
        password.send_keys(password_)
        password.send_keys(Keys.ENTER)

    def find_followers(self, similar_account):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_account}/")

        time.sleep(6)
        followers = self.driver.find_element(By.CSS_SELECTOR, ".xl565be:nth-child(2) ._aacl")
        followers.click()

        time.sleep(5)
        pop_up_window = self.driver.find_element(By.XPATH, '//div[2]/div/div/div/div/div[2]/div/div/div[2]')

        # Scroll till Followers list is there
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up_window)
            time.sleep(1)

    def follow(self):
        follow_buttons_list = self.driver.find_elements(By.CSS_SELECTOR, ".x1i10hfl .\_acan")
        for i in follow_buttons_list:
            try:
                i.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.CSS_SELECTOR, ".\_a9_1")
                cancel.click()
                time.sleep(2)
                continue
        time.sleep(10)



