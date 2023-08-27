import requests

response = requests.get("https://api.genderize.io?name=peter").json()

# data = response.json()

print(response)

