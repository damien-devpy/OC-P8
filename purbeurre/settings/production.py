from .base import *
from os import environ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'purbeurre_db',
        'USER': 'purbeurre_db_admin',
        'PASSWORD': environ.get('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
