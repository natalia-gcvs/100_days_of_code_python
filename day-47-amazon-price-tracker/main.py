import requests
from bs4 import BeautifulSoup
import smtplib
import os

user_email = os.environ['smtp_email']
password = os.environ['smtp_email_password']
recipient = os.environ['from_to_address']

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
          "Accept-Language": "en-US,en;q=0.9"}

response = requests.get("https://www.amazon.co.uk/dp/B0B1VR7BH2/ref=pe_27063361_485629781_TE_item", headers=header)

page_content = response.text

soup = BeautifulSoup(page_content, "html.parser")

lowest_price = 649.99
price = float(soup.select_one("span > .a-offscreen").getText()[1:])


if price <= 800:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=user_email, password=password)
        connection.sendmail(from_addr=user_email, to_addrs=recipient, msg=f"Subject:Laptop low price alert\n\n\n"
                                                                          f"The laptop price is now £{price}, below price set. "
                                                                          f"Go get it girl!".encode('utf-8'))

