"""List of database settings"""


class LocalPostgres:
    """Settings for a postgres db with default username and password"""
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'adventure',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '',
        },
    }


class SQLiteDatabase:
    """sqlite3 database settings"""
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'default.db',
        }
    }


class DummyDatabase:
    """dummy database settings"""
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.dummy',
            'NAME': 'default.db',
        },
    }
