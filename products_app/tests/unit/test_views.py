from django.shortcuts import reverse
from django.test import TestCase
from django.utils.encoding import smart_str


class TestSubstituteView(TestCase):

    def setUp(self):
        url = reverse('products_app:substitute', args=[42, ])
        self.response = self.client.get(url)

    def test_get_substitute_render_expected_template(self):
        assert self.response.status_code == 200
        assert 'products_app/substitute.html' in [template.name
                                                  for template
                                                  in self.response.templates
                                                  ]

    def test_get_subsitute_with_product_with_none_substitute_render_error_message(
            self):
        assert "Vous avez déjà le meilleur produit." in smart_str(
            self.response.content)


class TestProductView(TestCase):

    def setUp(self):
        url = reverse('products_app:product', args=[4242, ])
        self.response = self.client.get(url)

    def test_get_product_render_expected_template(self):
        assert self.response.status_code == 200
        assert 'products_app/product.html' in [template.name
                                               for template
                                               in self.response.templates
                                               ]

    def test_get_product_with_inexistent_id_return_error_message(self):
        assert "Ce produit n'existe pas." in smart_str(self.response.content)
