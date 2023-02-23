import requests
import os
from twilio.rest import Client

params = {"lat": -25.48,
          "long": -49.30,
          "appid": "be492f240bd37f9c8c1bb6a2c8a01c0b",
          }

api_key = os.environ.get("OWM_KEY_API")
auth_token = os.environ.get("SMS_AUTH_TOKEN")

response = requests.get("http://api.openweathermap.org/data/2.5/forecast?"
                        "lat=-25.48&lon=-49.30&appid=be492f240bd37f9c8c1bb6a2c8a01c0b")

print(response.status_code)
print(response)
weather_data = response.json()['list']
print(weather_data)


weather_forecast = [{"weather": i["weather"], "dt_txt": i["dt_txt"]} for i in weather_data]
print(weather_forecast[0]['dt_txt'])

rain_forecast = ["Bring an umbrella" for index, i in enumerate(weather_forecast[:9]) for n in i["weather"] if n['id'] < 799]

if "Bring an umbrella" in rain_forecast:
    client = Client(api_key, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella",
        from_="+19788506384",
        to="+353833126285"
    )

print(message.status)