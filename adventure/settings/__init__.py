from split_settings.tools import include
from os import environ


ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'environments/local.py',
]

include(*base_settings)

