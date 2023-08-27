##################### Extra Hard Starting Project ######################
import random
import pandas as pd
import datetime as dt
import smtplib
import time


# 1. Update the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month

my_email = "email@gmail.com"
password = 'youpassword'

birthdays = pd.read_csv("birthdays.csv")
PLACEHOLDER = "[NAME]"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)

# 2. Check if today matches a birthday in the birthdays.csv
for index, row in birthdays.iterrows():
    if row['day'] == day and row['month'] == month:
        recipient = row['email']
        name = row['name']
        random_letter = random.randint(1, 3)
        # 3. If step 2 is true, pick a random letter from letter templates and replace
        # the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random_letter}.txt", port=587) as letter:
            content = letter.read()
            new_content = content.replace(PLACEHOLDER, name)
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=f"Subject:Happy Birthday\n\n\n{new_content}")











