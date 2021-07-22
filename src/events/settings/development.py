from events.settings.base import *
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application

DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['django_extensions']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS'] = None
REST_FRAMEWORK['PAGE_SIZE'] = None

STATICFILES_DIRS = [
    BASE_DIR / 'static/',
]
