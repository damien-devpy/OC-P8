from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)


class Product(models.Model):
    """Contain all informations about a product."""

    barre_code = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=300)
    nutriscore = models.CharField(max_length=1)
    pict_product = models.CharField(max_length=150)
    pict_nutriments = models.CharField(max_length=150)
    # Nutriments
    energy_kj = models.CharField(max_length=50)
    energy_kcal = models.CharField(max_length=50)
    lipid = models.CharField(max_length=50)
    glucid = models.CharField(max_length=50)
    fiber = models.CharField(max_length=50)
    protein = models.CharField(max_length=50)
    salt = models.CharField(max_length=50)

    categories = models.ManyToManyField(Category)
