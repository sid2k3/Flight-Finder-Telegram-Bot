import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
import os
from dotenv import load_dotenv

load_dotenv("keys.env")

API_KEY = os.environ["API_KEY"]
API_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
CURR = "INR"
head = {
    "apikey": API_KEY
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, code, price, city_to, from_code, from_city, months):
        # self.sheet_data = sheet_data
        self.from_code = from_code
        self.from_city = from_city
        self.months = months
        self.code = code
        self.price = price
        self.all_flights_data = {"max_price": price, "from": from_city, "to": city_to, "data": []}

    def find_flights(self):
        city_code = self.code
        now = dt.datetime.now()
        date_from = now.strftime("%d/%m/%Y")
        date_to = dt.date.today() + relativedelta(months=+ self.months)
        date_to = date_to.strftime("%d/%m/%Y")
        pars = {

            "fly_from": self.from_code,
            "fly_to": self.code,
            "date_from": date_from,
            "date_to": date_to,
            "curr": "INR",
            "asc": 1

        }
        # print(pars)
        # print(head)
        response = requests.get(url=API_ENDPOINT, params=pars, headers=head)
        response.raise_for_status()
        # print(response.json())
        # print("okok")
        return response.json()

    def get_relevant_data(self):
        date_set = set()

        response = self.find_flights()
        for flight in response["data"]:
            temp_price = flight["price"]
            temp_date = str(flight["local_departure"]).split("T")[0]
            temp_date = "-".join(temp_date.split("-")[::-1])
            temp_duration = flight["duration"]["total"] / 3600
            temp_duration = round(temp_duration, 2)
            if temp_date not in date_set:
                if temp_price <= self.price:
                    date_set.add(temp_date)
                    self.all_flights_data["data"].append(
                        f"{temp_date} ->  {temp_price}₹, Duration: {temp_duration} hours")
        return self.all_flights_data
