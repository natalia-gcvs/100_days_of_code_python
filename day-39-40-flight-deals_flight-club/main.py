from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

ORIGIN_CITY_IATA_CODE = "CWB"
initial_date = datetime.now() + timedelta(days=1)
final_date = initial_date + timedelta(days=6*30)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
user_data = data_manager.get_users_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for city in sheet_data:
        city["iataCode"] = flight_search.get_destination_code(city["city"])
        data = flight_search.search_cheap_flights(city)
    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()


for destination in sheet_data:
    flight = flight_search.search_cheap_flights(
                                  ORIGIN_CITY_IATA_CODE,
                                  destination["iataCode"],
                                  initial_date,
                                  final_date
    )
    if flight is None:
        continue
    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} " \
                  f"to {flight.return_date}."
        print(message)

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        link = f"https://www.google.com.br/flights?hl=pt-PT#flt={flight.origin_airport}." \
               f"{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}." \
               f"{flight.origin_airport}.{flight.return_date}"

        print(link)

        for user in user_data:
            recipient = user['email']
            name = f"{user['firstName']} {user['lastName']}"
            notification_manager.send_emails(user_email=recipient, user_name=name, msg=message)

        notification_manager.send_message(
            message=f"Low price alert! Only £{flight.price} to fly from "
                    f"{flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city}-{flight.destination_airport}, from "
                    f"{flight.out_date} to {flight.return_date}."
        )











