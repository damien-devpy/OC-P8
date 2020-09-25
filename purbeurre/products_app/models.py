from django.db import models

class Product(models.Model):
    """Contain all informations about a product."""

    barre_code = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=300)
    nutriscode = models.CharField(max_length=1)
