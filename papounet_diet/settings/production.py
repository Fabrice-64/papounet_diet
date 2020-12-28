import dj_database_url

from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Requested for deployment with Heroku, when using PostgreSQL
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
