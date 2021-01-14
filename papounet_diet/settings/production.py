from .base import *

DEBUG = False

ADMINS = {
    ('Fabrice J', 'fabricejaouen@yahoo.com'),
}

ALLOWED_HOSTS = ['159.89.0.27']

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',

    }
}
