from requests import get as requests_get

from .configuration import ENDPOINT, TAGS


class Downloader:
    """Manage the OpenFoodFacts API. Download data from the endpoints"""

    def __init__(self, page):
        """Create a Downloader object.

        Attributes:
            self.page (int): Page of 1000 products to get from API

        """

        self.page = page

    def get_data(self):
        """Call API and download products. Return JSON data.

        Returns:
            json_data (JSON): JSON data from OpenFoodFacts API

        """
        TAGS['page'] = self.page

        json_data = requests_get(ENDPOINT, params=TAGS).json()

        return json_data

    @property
    def json(self):
        return self.get_data()
