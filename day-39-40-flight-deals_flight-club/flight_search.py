import requests
from flight_data import FlightData
from pprint import pprint

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
                      "curr": "BRL",
                      }
            response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', params=params, headers=headers)
            try:
                data = response.json()["data"][0]
            except IndexError:
                try:
                    params["max_stopovers"] = 1
                    response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', params=params, headers=headers)
                    data = response.json()["data"][0]
                    flight_data = FlightData(
                        price=data["price"],
                        origin_city=data["cityFrom"],
                        origin_airport=data["flyFrom"],
                        destination_city=data["cityTo"],
                        destination_airport=data["flyTo"],
                        out_date=data["route"][0]["local_departure"].split("T")[0],
                        return_date=data["route"][1]["local_departure"].split("T"),
                        stop_overs=1,
                        via_city=data["route"][0]["cityTo"])
                    print(f"{flight_data.destination_city}: £{flight_data.price}")

                    return flight_data

                except IndexError:
                    print(f"No flights found for {destination_code}.")
                    return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=0,
                    via_city=""

                )


                print(f"{flight_data.destination_city}: £{flight_data.price}")

                return flight_data



