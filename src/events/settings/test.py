from events.settings.base import * # noqa

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}
SOUTH_TESTS_MIGRATE = False

REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS'] = None
REST_FRAMEWORK['PAGE_SIZE'] = None
