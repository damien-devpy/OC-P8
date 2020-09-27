from django.core.management.base import BaseCommand
from products_app.models import Product, Category

from .load_db.downloader import Downloader
from .load_db.sort import Sort


class Commande(BaseCommand):
    help = 'Populate product and category tables. ' \
           'You have to specify a number of products. ' \
           '"python manage.py load_db 3000" for example.' \

    def add_arguments(self, parser):
        parser.add_argument('products')

    def handle(self, *args, **options):
        how_much_products = options['products']

        download = Downloader(how_much_products)
        data = download.json

        data_sorted_out = Sort(data)

        for product in data_sorted_out.products:
            p = Product(**product['informations'])
            p.save()
            p.add(Category(c).save for c in product['categories'])
