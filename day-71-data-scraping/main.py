from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

# set up chrome options
chrome_options = Options()
chrome_options.add_argument('--headless') # run the browser in headless mode (without GUI)

# initialize the driver with chrome options
driver = webdriver.Chrome(options=chrome_options)

# navigate to the target URL
target_url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'
driver.get(target_url)

# scroll to the end of the page
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
time.sleep(5)

# extract the HTML source code of the page
resp = driver.page_source

# close the driver
driver.quit()

# parse the HTML source code using BeautifulSoup
soup = BeautifulSoup(resp, 'html.parser')

table = soup.find('table', {'class': 'data-table'})

# Extract the data you want from the table using BeautifulSoup and Store the table data in a dictionary
data = {}
rows = table.find_all('tr')
for i, row in enumerate(rows):
    cells = row.find_all('td')
    # Store the cells in a list
    data[i] = [cell.find('span', class_="data-table__value").text for cell in cells]


# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# Set the column names to the text content of the header row
header_row = table.find('tr')
headers = [header.text for header in header_row.find_all('th')]
df.columns = headers

# Print the DataFrame
print(df)

df.to_csv('salaries_by_college_major2.csv', index=False)



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