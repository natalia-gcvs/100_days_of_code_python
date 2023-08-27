from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# set up chrome options
chrome_options = Options()
chrome_options.add_argument('--headless') # run the browser in headless mode (without GUI)

# initialize the driver with chrome options
driver = webdriver.Chrome(options=chrome_options)

# set the base URL and initial page number
base_url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'
page_num = 1

driver.get(base_url)

#scroll to the end of the page
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
time.sleep(5)

# extract the HTML source code of the page
resp = driver.page_source

# parse the HTML source code using BeautifulSoup
soup = BeautifulSoup(resp, 'html.parser')

pagination = soup.find('div', class_='pagination csr-gridpage__pagination')

pages = pagination.find_all('div', class_='pagination__btn--inner')

numeric_list = [page.text for page in pages if page.text.isdigit()]

last_page = int(numeric_list[-1])
print(type(last_page))
print(type(page_num))

# initialize an empty list to store the data from all pages
all_data = []

while page_num <= last_page:
    # navigate to the target URL
    target_url = base_url + '/page/' + str(page_num)
    print(f"Extracting data from page {page_num} ({target_url})")
    driver.get(target_url)

    # scroll to the end of the page
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    time.sleep(5)

    # extract the HTML source code of the page
    resp = driver.page_source

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

    # append the data from the current page to the list of all data
    all_data.extend(list(data.values()))
    print(all_data)

    page_num += 1


# close the driver
driver.quit()

# convert the list of data to a pandas DataFrame
df = pd.DataFrame(all_data, columns=['Rank', 'Major', 'Degree Type', 'Early Career Pay', 'Mid-Career Pay', '% High Meaning'])

# print the DataFrame
print(df)

df.to_csv('salaries_by_college_major2.csv', index=False)