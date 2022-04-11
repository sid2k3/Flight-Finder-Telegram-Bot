class FlightData:
    def __init__(self, flight_data):
        self.flight_data = flight_data
        self.message = ""

    def generate_formatted_message(self):
        city_from = self.flight_data["from"]
        city_to = self.flight_data["to"]
        if len(self.flight_data["data"]) != 0:
            self.message = f"Cheaper Flights from {city_from} to {city_to} are now available on these dates:-\n"
            for flight in self.flight_data["data"]:
                self.message += f"{flight}\n"
        else:
            self.message = f"Currently no flights are available with price less than {self.flight_data['max_price']} " \
                           f"from {city_from} to {city_to}.\n"
        return self.message
