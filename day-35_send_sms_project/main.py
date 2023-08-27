import requests
import os
from twilio.rest import Client

params = {"lat": -25.48,
          "long": -49.30,
          "appid": os.environ.get("OWM_KEY_API")
          }
APPID = os.environ.get("OWM_KEY_API")
TWL_ID = os.environ.get("TWL_ID")
TWL_AUTH_TOKEN = os.environ.get("SMS_AUTH_TOKEN")
TWL_VIRTUAL_NUM = os.environ.get("TWL_VIRTUAL_NUM")
TWL_VERIFIED_NUM = os.environ.get("TWL_VERIFIED_NUM")

print(os.environ.get("OWM_KEY_API"))

response = requests.get("http://api.openweathermap.org/data/2.5/forecast?"
                        "lat=-25.48&lon=-49.30&appid=APPID")

print(response.status_code)
print(response)
weather_data = response.json()['list']
print(weather_data)


weather_forecast = [{"weather": i["weather"], "dt_txt": i["dt_txt"]} for i in weather_data]
print(weather_forecast[0]['dt_txt'])

rain_forecast = ["Bring an umbrella" for index, i in enumerate(weather_forecast[:9]) for n in i["weather"] if n['id'] < 799]

if "Bring an umbrella" in rain_forecast:
    client = Client(TWL_ID, TWL_AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Bring an umbrella",
        from_=TWL_VIRTUAL_NUM,
        to=TWL_VERIFIED_NUM
    )

print(message.status)