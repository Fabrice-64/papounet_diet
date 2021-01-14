from .base import *

DEBUG = False

ADMINS = {
    ('Fabrice J', 'fabricejaouen@yahoo.com'),
}

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',

    }
}
