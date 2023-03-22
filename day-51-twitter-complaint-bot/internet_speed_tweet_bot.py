import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InternetSpeedTweetBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=ChromeOptions())
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(5)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        # get download and upload speed
        time.sleep(50)
        self.down = float(self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                             '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)

        self.up = float(self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/'
                                           'div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)



    def tweet_at_provider(self, email, username, password, promised_down, promised_up):
        if self.down <= promised_down * 0.90 and self.up <= promised_up * 0.90:

            self.driver.get("https://twitter.com/i/flow/login")

            time.sleep(5)
            email_login = self.driver.find_element(By.NAME, 'text')
            email_login.send_keys(email)
            email_login.send_keys(Keys.ENTER)

            time.sleep(5)
            username_login = self.driver.find_element(By.NAME, 'text')
            username_login.send_keys(username)
            username_login.send_keys(Keys.ENTER)

            time.sleep(5)
            password_login = self.driver.find_element(By.NAME, 'password')
            password_login.send_keys(password)
            password_login.send_keys(Keys.ENTER)

            time.sleep(5)
            tweet_compose = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')
            tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {promised_down}down/{promised_up}up?"
            tweet_compose.send_keys(tweet)

            tweet_button = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-1vtznih.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span')
            tweet_button.click()

            time.sleep(2)
            self.driver.quit()
        else:
            print(f"The internet speed was within the promised speed {self.down}down/{self.up}up")
