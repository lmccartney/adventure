"""List of database settings"""
import os

LOCAL = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'adventure',
    'USER': 'adventure_app',
    'PASSWORD': os.environ.get('DEV_DB_PW'),
    'HOST': 'localhost',
    'PORT': '',
}

CI = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'test_db',
}
