import time
import requests
from datetime import datetime
import smtplib

MY_LAT = -25.480877 # Your latitude
MY_LONG = -49.304424 # Your longitude

USER = "natalia.gcvs@gmail.com"
PASSWORD = 'ivykmwyixvrlkfum'

#Your position is within +5 or -5 degrees of the ISS position.
def positions_proximity():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    return time_now >= sunset or time_now < sunrise


# run the code every 60 seconds.
while True:
    time.sleep(60)
    #If the ISS is close to my current position and it is currently dark
    if positions_proximity() and is_night():
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(from_addr=USER, to_addrs='natalia.gcvs@gmail.com', msg=f"Subject: ISS Current Position \n\n\nLook up!")






