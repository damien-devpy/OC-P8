from django.core.management import call_command
from django.test import TestCase
from products_app.models import Product


class TestLoadDBCommand(TestCase):
    def test_that_load_db_load_expected_products(self):
        call_command('loaddb', '42')
        how_much_products_loaded = Product.objects.all().count()

        assert how_much_products_loaded == 42

    def test_that_load_db_load_expected_products2(self):
        call_command('loaddb', '1337')
        how_much_products_loaded = Product.objects.all().count()

        assert how_much_products_loaded == 1337
