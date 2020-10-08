from django.shortcuts import reverse
from django.test import TestCase
from django.utils.encoding import smart_str
from products_app.models import Product


class TestPostSearch(TestCase):

    def setUp(self):
        product = Product.objects.create(barre_code=42,
                                         name="Coca-Cola",
                                         nutriscore="e",
                                         pict_product="random_url",
                                         pict_nutriments="random_url",
                                         energy_kj="value",
                                         energy_kcal="value",
                                         lipid="value",
                                         glucid="value",
                                         fiber="value",
                                         protein="value",
                                         salt="value", )

    def test_post_return_results(self):
        url = reverse('search_app:results')
        response = self.client.post(url, {'input_user': 'coca'})

        assert "Coca-Cola" in smart_str(response.content)
        assert "nutriscore e" in smart_str(response.content)
