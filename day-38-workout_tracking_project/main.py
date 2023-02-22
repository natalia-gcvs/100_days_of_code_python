import requests
from datetime import datetime
import os

user_log = input("Tell me which exercises you did: ")

GENDER = "female"
WEIGHT_KG = 58
HEIGHT_CM = 163
AGE = 31

SHEETY_ENDPOINT = "https://api.sheety.co/081ff0568abe24131136fb9e35b2406c/workoutTracking/workouts"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ID = os.environ.get("SHEETY_ID")
SHEETY_PASSWORD =os.environ.get("SHEETY_PASSWORD")

API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")

HEADERS = {"x-app-id": API_ID,
           "x-app-key": API_KEY,
           }
NUTRITIONIX_PARAMS = {
    "query": user_log,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=NUTRITIONIX_PARAMS, headers=HEADERS)
exercise_data = response.json()

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

for exercise in exercise_data['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, auth=(SHEETY_ID, SHEETY_PASSWORD))

print(sheet_response.text)
