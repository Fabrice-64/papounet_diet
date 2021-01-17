from .base import *
import sentry_sdk


DEBUG = False

ADMINS = {
    ('Fabrice J', 'fabricejaouen@yahoo.com'),
}

ALLOWED_HOSTS = ['206.189.55.69', 'localhost']

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',

    }
}


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')