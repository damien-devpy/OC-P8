from django.core.management.base import BaseCommand
from django.db import IntegrityError, DataError
from products_app.models import Product, Category

from .load_db.downloader import Downloader
from .load_db.sort import Sort
import pdb

class Command(BaseCommand):
    help = """Populate product and category tables.
           You have to specify a number of products.
           "python manage.py load_db 3000" for example."""

    def add_arguments(self, parser):
        parser.add_argument('products', type=int)

    def handle(self, *args, **options):
        page = 1
        product_count = 0

        while True:
            if product_count == 0:
                self.stdout.write('Loading database...')
            self.stdout.write('Calling OpenFoodFacts API')

            download = Downloader(page)
            data = download.json

            data_sorted_out = Sort(data)
            self.stdout.write('Downloaded and sorted out 1000 products')

            for product in data_sorted_out.products:
                if product_count < options['products']:
                    try:
                        p = Product.objects.create(**product['informations'])
                        product_count += 1
                    except IntegrityError:
                        continue

                    categories = (Category.objects.update_or_create(name=c)[0]
                                  for c in product['categories']
                                  )
                    p.categories.add(*categories)

                else:
                    break

                if not (product_count % 100):
                    self.stdout.write(f'{product_count} products registered.')

            if product_count>= options['products']:
                break

            page += 1

        products = Product.objects.all()
        self.stdout.write(self.style.SUCCESS(f'Successfully saved {product_count} products in database.'))
