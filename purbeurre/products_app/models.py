from django.core.validators import MinValueValidator
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
    energy_kj = models.IntegerField(validators=[MinValueValidator(0)])
    energy_kcal = models.IntegerField(validators=[MinValueValidator(0)])
    lipid = models.FloatField(validators=[MinValueValidator(0)])
    glucid = models.FloatField(validators=[MinValueValidator(0)])
    fiber = models.FloatField(validators=[MinValueValidator(0)])
    protein = models.FloatField(validators=[MinValueValidator(0)])
    salt = models.FloatField(validators=[MinValueValidator(0)])

    categories = models.ManyToManyField(Category)
