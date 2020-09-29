from django.core.management import call_command
from django.test import TestCase
from products_app.models import Product


class TestLoadDBCommand(TestCase):
    def test_that_command_load_db_with_minimum_1000_products(self):
        call_command('loaddb', '100')
        how_much_products_loaded = len(Product.objects.all())

        assert how_much_products_loaded == 1000

    def test_that_load_db_load_expected_products(self):
        call_command('loaddb', '1042')
        how_much_products_loaded = len(Product.objects.all())

        assert how_much_products_loaded == 1042
