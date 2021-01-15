from .base import *
from django.core.management.utils import get_random_secret_key

DEBUG = True
SECRET_KEY = get_random_secret_key()
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


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')