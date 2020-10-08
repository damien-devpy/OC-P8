from django.test import TestCase
from django.shortcuts import reverse
from django.utils.encoding import smart_str
from products_app.models import Product
from users_app.models import User


class TestFavoritesView(TestCase):

    def setUp(self):
        url = reverse('users_app:signup')
        self.credentials = {'email': 'new_user@gmail.com',
                       'password1': 'r4nd0mp4ssw0rd',
                       'password2': 'r4nd0mp4ssw0rd',
                       }

        self.client.post(url, self.credentials)

    def test_get_favorites_with_favorites_register_return_expected_favorites(self):
        product = Product.objects.create(barre_code=42,
                                         name="Specific product",
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

        current_user = User.objects.get(email=self.credentials['email'])
        current_user.favorites.add(product)

        url = reverse('favorites_app:favorites')
        self.response = self.client.get(url)

        assert "Mes aliments" in smart_str(self.response.content)
        assert product.name in smart_str(self.response.content)


    def test_post_favorites_return_expected_favorites_product(self):
        product = Product.objects.create(barre_code=42,
                                         name="Specific product2",
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

        url = reverse('favorites_app:favorites')

        self.response = self.client.post(url, {'product_substitute': product.id})

        assert "Mes aliments" in smart_str(self.response.content)
        assert product.name in smart_str(self.response.content)
