import requests
from dotenv import load_dotenv
import os

load_dotenv("keys.env")
FLIGHT_API_KEY = os.environ["API_KEY"]
FLIGHT_LOCATION_API_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

head = {
    "apikey": FLIGHT_API_KEY
}


class DataManager:
    def __init__(self, data):
        self.data = data
        self.codes_prices = []
        self.get_iata()
        print(self.data)

    def get_iata(self):
        pars = {
            "term": self.data["to"],
            "limit": 1,
            "location_types": "city"
        }
        print(pars)
        response = requests.get(FLIGHT_LOCATION_API_ENDPOINT, params=pars, headers=head)
        response.raise_for_status()
        to_iata = response.json()["locations"][0]["code"]
        self.data["to_code"] = to_iata
        pars["term"] = self.data["from"]
        response = requests.get(FLIGHT_LOCATION_API_ENDPOINT, params=pars, headers=head)
        response.raise_for_status()
        print(pars)
        from_iata = response.json()["locations"][0]["code"]
        #
        # if from_iata is None or to_iata is None:
        #     pass

        self.data["from_code"] = from_iata

    def get_data(self):
        return self.data
