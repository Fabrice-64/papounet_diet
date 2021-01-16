from .base import *
from django.core.management.utils import get_random_secret_key

DEBUG = True
SECRET_KEY = get_random_secret_key()
ADMINS = {
    ('Fabrice J', 'fabricejaouen@yahoo.com'),
}

ALLOWED_HOSTS = ['206.189.55.69', 'localhost']

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'papounet_diet_db',
        'USER': 'fabrice',
        'PASSWORD': '@HaRiBo2021',
        'HOST': 'localhost',
        'PORT': '',

    }
}


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')