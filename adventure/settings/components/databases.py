"""List of database settings"""

LOCAL = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'adventure',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': 'localhost',
    'PORT': '',
}

CI = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'test_db',
}
