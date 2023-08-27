from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time


listings = {}

driver = webdriver.Chrome(options=ChromeOptions())


# target_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
#              "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A" \
#              "-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C" \
#              "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A" \
#              "%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse" \
#              "%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B" \
#              "%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D" \
#              "%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min" \
#              "%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D "
#
# driver.get(target_url)
# time.sleep(2)
# html = driver.find_element(By.TAG_NAME, 'html')
# html.send_keys(Keys.END)
#
# time.sleep(5)
# resp = driver.page_source
# driver.close()
# soup = BeautifulSoup(resp, 'html.parser')
#
# time.sleep(1)
# listings_elements = soup.select(selector='#grid-search-results > ul > li')
#
#
# for key, listing in enumerate(listings_elements):
#     try:
#         listings[key] = {'address': listing.select_one(" a > address").getText(),
#                          'price': int(listing.select_one(
#                              ".StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0.bqsBln > span").getText().split(
#                              "+")[0][1:].replace(",", "").replace("/mo", "")),
#                          'link': f'https://www.zillow.com/{listing.select_one(".StyledPropertyCardPhotoBody-c11n-8-85-1__sc-128t811-0.juCZCh > a").get("href")}'}
#     except AttributeError:
#         pass
#
# with open("data.json", "w") as file:
#     json.dump(listings, file, indent=4)

with open("data.json", "r") as file:
    listings_data = json.load(file)


for key, listing in listings_data.items():
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd6uZ58qh2m9MoYQFdgMlNIhBc_c5NpKPAzPzJtA_WItDcT3A/viewform?usp=sf_link")

    time.sleep(2)
    property_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    property_address.send_keys(listing['address'])
    property_price.send_keys(listing['price'])
    property_link.send_keys((listing['link']))
    submit_button.click()




