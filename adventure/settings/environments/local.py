"""
Django settings for adventure project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from .utils import SettingsLoader
from .components import databases, base


class LocalMetaSettings(databases.SQLiteDatabase, base.BaseSettings):
    pass


class LocalSettings(SettingsLoader, databases.SQLiteDatabase, base.BaseSettings):
    SECRET_KEY = 'abc123'


LocalSettings.load_settings(__name__)
