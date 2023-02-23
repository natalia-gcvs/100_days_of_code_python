import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "sXlgq2aZRqJ7E--BdnKZqnvavTpz-LPE"


class FlightSearch:

    def get_destination_code(self, city_name):
        headers = {"apikey": TEQUILA_API_KEY}
        params = {"term": city_name,
                  "location_types": "city",
                  }
        response = requests.get(url=f'{TEQUILA_ENDPOINT}/locations/query', headers=headers, params=params)
        code = response.json()["locations"][0]["code"]
        return code

    def search_cheap_flights(self, departure_from, destination_code, initial_date, final_date):
            headers = {"apikey": TEQUILA_API_KEY}
            params = {"fly_from": departure_from,
                      "fly_to": destination_code,
                      "date_from": initial_date.strftime("%d/%m/%Y"),
                      "date_to": final_date.strftime("%d/%m/%Y"),
                      "nights_in_dst_from": 7,
                      "nights_in_dst_to": 28,
                      "flight_type": "round",
                      "one_for_city": 1,
                      "max_stopovers": 0,
                      "curr": "GBP",
                      }
            response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', params=params, headers=headers)

            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f'No flights found for {destination_code}.')
                return None

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")

            )

            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data



