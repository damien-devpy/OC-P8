from .configuration import ENDPOINT, TAGS
from requests import get as requests_get

class Downloader:
    """Manage the OpenFoodFacts API. Download data from the endpoints"""

    def __init__(self, products):
        """Create a Downloader object.

        Attributes:
            self.products (int): How much products has to be download.

        """

        self.products = products

    def get_json_data(self):
        """Call API and download products. Return JSON data.

        Returns:
            json_data (JSON): JSON data from OpenFoodFacts API

        """
        json_data = requests_get(ENDPOINT, params=TAGS)

        return json_data

    @property
    def json(self):
        return self.get_json_data()
