from django.test import TestCase
from django.shortcuts import reverse
from django.utils.encoding import smart_str
from products_app.models import Product, Category

class TestSubstituteView(TestCase):

    def setUp(self):

        Category.objects.bulk_create([
            Category(name='Pâte à tartiner'),
            Category(name='Petit-déjeuner'),
        ])

        self.categories = Category.objects.all()

        self.product_to_sub = Product.objects.create(barre_code=42,
                                         name="Nutella",
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

        self.product_to_sub.categories.add(self.categories[0])
        self.product_to_sub.categories.add(self.categories[1])

        self.product_substitute = Product.objects.create(barre_code=43,
                                         name="Meilleure pâte à tartiner",
                                         nutriscore="a",
                                         pict_product="random_url",
                                         pict_nutriments="random_url",
                                         energy_kj="value",
                                         energy_kcal="value",
                                         lipid="value",
                                         glucid="value",
                                         fiber="value",
                                         protein="value",
                                         salt="value", )

        self.product_substitute.categories.add(self.categories[0])
        self.product_substitute.categories.add(self.categories[1])

        url = reverse('products_app:substitute', args=[self.product_to_sub.id])

        self.response = self.client.get(url)

    def test_get_substitute_with_product_with_better_substitute_return_substitute(self):
        # pdb.set_trace()
        assert self.product_substitute.name in smart_str(self.response.content)
        assert "nutriscore a" in smart_str(self.response.content)

class TestProductView(TestCase):

    def test_get_product_with_existent_id_return_correct_product(self):
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

        url = reverse('products_app:product', args=[product.id,])
        self.response = self.client.get(url)

        assert product.name in smart_str(self.response.content)
