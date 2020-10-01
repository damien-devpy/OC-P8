from django.core.management.base import BaseCommand
from django.db import IntegrityError
from products_app.models import Product, Category

from .load_db.downloader import Downloader
from .load_db.sort import Sort


class Command(BaseCommand):
    help = """Populate product and category tables.
           You have to specify a number of products.
           "python manage.py load_db 3000" for example."""

    def add_arguments(self, parser):
        parser.add_argument('products', type=int)

    def handle(self, *args, **options):
        if options['products'] < 1000:
            options['products'] = 1000

        page = 1
        product_count = 0

        while product_count < options['products']:
            if product_count == 0:
                self.stdout.write('Loading database...')
            self.stdout.write('Calling OpenFoodFacts API')

            download = Downloader(page)
            data = download.json

            data_sorted_out = Sort(data)
            self.stdout.write('Downloaded and sorted out 1000 products')

            for product in data_sorted_out.products:
                if all((not (product_count % 100),
                        product_count > 0)
                       ):
                    self.stdout.write(f'{product_count} products registered.')

                if product_count < options['products']:
                    p = Product.objects.get_or_create(**product['informations'])[0]
                    product_count += 1

                    # Tying current product to each one of his categories
                    categories = (Category.objects.get_or_create(name=c)[0]
                                  for c in product['categories'])
                    p.categories.add(*categories)
                else:
                    break

            page += 1


        self.stdout.write(
            f'Successfully saved {Product.objects.all().count()} products in database.')
