# Generated by Django 3.1.1 on 2020-09-25 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('barre_code', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=300)),
                ('nutriscore', models.CharField(max_length=1)),
                ('pict_url', models.CharField(max_length=150)),
                ('pict_nutriments', models.CharField(max_length=150)),
                ('energy_kj', models.IntegerField(
                    validators=[django.core.validators.MinValueValidator(0)])),
                ('energy_kcal', models.IntegerField(
                    validators=[django.core.validators.MinValueValidator(0)])),
                ('lipid', models.FloatField(
                    validators=[django.core.validators.MinValueValidator(0)])),
                ('glucid', models.FloatField(
                    validators=[django.core.validators.MinValueValidator(0)])),
                ('fiber', models.FloatField(
                    validators=[django.core.validators.MinValueValidator(0)])),
                ('protein', models.FloatField(
                    validators=[django.core.validators.MinValueValidator(0)])),
                ('salt', models.FloatField(
                    validators=[django.core.validators.MinValueValidator(0)])),
                ('category',
                 models.ManyToManyField(to='products_app.Category')),
            ],
        ),
    ]
