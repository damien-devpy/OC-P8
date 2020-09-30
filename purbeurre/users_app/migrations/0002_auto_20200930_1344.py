# Generated by Django 3.1.1 on 2020-09-30 11:44

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Adresse électronique'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name="Nom d'utilisateur"),
        ),
    ]
