from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from products_app.models import Product


class User(AbstractUser):
    """Custom model of an User."""
    username_validator = UnicodeUsernameValidator()

    # Custom user name field. Making it optionnal.
    username = models.CharField(_('Nom d\'utilisateur'),
                                max_length=150,
                                validators=[username_validator],
                                blank=True)

    email = models.EmailField(_('Adresse électronique'),
                              unique=True)
    favorites = models.ManyToManyField(Product, db_table="favorite")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        # If user has record an username, display it.
        if bool(self.username):
            return f'{self.username}'
        # Otherwise display it's email
        return f'{self.email}'
