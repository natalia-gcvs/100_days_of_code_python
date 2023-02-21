import requests

response = requests.get(f"https://opentdb.com/api.php?amount=10&type=boolean")
question_data = response.json()['results']
