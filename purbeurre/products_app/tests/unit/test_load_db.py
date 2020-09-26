from django.test import TestCase
from products_app.management.commands.load_db.downloader import Downloader


class TestDownloader(TestCase):

    def test_create_downloader_that_take_an_int(self):
        download = Downloader(42)
        self.assertEqual(download.products, 42)

    def test_downloader_return_expected_data(self, monkeypatch):

        monkeypatch.setattr(
            ""
        )

        download = Downloader(1)
        data = download.json
        expected_data = {
            'products': [{
                'product_name_fr': 'Prince goût chocolat au blé complet',
                'code': '7622210449283',
                'categories': 'Snacks, Snacks sucrés, B…cuits, Biscuits fourrés',
                'nutrition_grade_fr': 'd',
                'image_url': 'https://static.openfoodf…283/front_fr.286.400.jpg',

            }]
        }
        self.assertEqual(data, expected_data)


class TestSort(TestCase):
    pass

class TestLoadDB(TestCase):
    pass