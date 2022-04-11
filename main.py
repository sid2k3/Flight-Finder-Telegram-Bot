from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
import telegram_bot


def process_query(data):
    data_manager_obj = DataManager(data)
    data = data_manager_obj.get_data()
    flight_search_obj = FlightSearch(data["to_code"], data["price"], data["to"], data["from_code"], data["from"],
                                     data["months"])
    relevant_data = flight_search_obj.get_relevant_data()
    flight_data_obj = FlightData(relevant_data)
    message = flight_data_obj.generate_formatted_message()
    return message


if __name__ == "__main__":
    telegram_bot.start_bot()
