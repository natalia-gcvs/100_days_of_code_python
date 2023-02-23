from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

destination_code = "LON"
initial_date = datetime.now() + timedelta(days=1)
final_date = initial_date + timedelta(days=6*30)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

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
                              destination_code,
                              destination["iataCode"],
                              initial_date,
                              final_date
    )
    if flight.price < destination_code["lowestPrice"]:
        notification_manager.send_message(
            message=f"Low price alert! Only £{flight.price} to fly from "
                    f"{flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city}-{flight.destination_airport}, from "
                    f"{flight.out_date} to {flight.return_date}."
        )









