import logging

import requests

from .exceptions import CannotGetPrice

logger = logging.getLogger(__name__)


class GateClient:
    PRICE_URL = "https://data.gateapi.io/api2/1/ticker/rei_usdt"

    def __init__(self):
        self.http_session = requests.Session()

    def get_rei_usd_price(self) -> float:
        try:
            response = self.http_session.get(self.PRICE_URL, timeout=10)
            api_json = response.json()
            price = float(api_json["last"])
            return price
        except (ValueError, IOError) as e:
            raise CannotGetPrice from e
