from products_app.management.commands.load_db.downloader import Downloader

from .mock_requests_get import MockRequests


def test_create_downloader_that_take_an_int():
    download = Downloader(1)
    assert download.page == 1


def test_downloader_return_expected_data(monkeypatch):
    monkeypatch.setattr(
        "products_app.management.commands.load_db.downloader.requests_get",
        MockRequests,
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
    assert expected_data == data
