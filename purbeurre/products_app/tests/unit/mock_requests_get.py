class MockRequests:
    """Mock requests get method."""

    def __init__(self, *args, **kwargs):
        pass

    def json(self):
        results = {
            'products': [{
                'product_name_fr': 'Prince goût chocolat au blé complet',
                'code': '7622210449283',
                'categories': 'Snacks, Snacks sucrés, B…cuits, Biscuits fourrés',
                'nutrition_grade_fr': 'd',
                'image_url': 'https://static.openfoodf…283/front_fr.286.400.jpg',

            }]
        }

        return results
