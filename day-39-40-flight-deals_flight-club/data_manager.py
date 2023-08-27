import requests

SHEET_FLIGHTS_ENDPOINT = os.environ['SHEET_FLIGHTS_ENDPOINT']
SHEET_USERS_ENDPOINT = os.environ['SHEET_USERS_ENDPOINT']


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_FLIGHTS_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            code = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f'{SHEET_FLIGHTS_ENDPOINT}/{city["id"]}', json=code)
        print(response.text)

    def get_users_data(self):
        response = requests.get(url=SHEET_USERS_ENDPOINT)
        data = response.json()["users"]
        return data











