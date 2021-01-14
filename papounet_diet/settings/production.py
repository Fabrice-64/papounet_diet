from .base import *

DEBUG = False

ADMINS = {
    ('Fabrice J', 'fabricejaouen@yahoo.com'),
}

ALLOWED_HOSTS = ['159.89.0.27']

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'papounet_diet',
        'USER': 'papounet_diet_user',
        'PASSWORD': '@HaRiBo2021',
        'HOST': 'localhost',
        'PORT': '',

    }
}
