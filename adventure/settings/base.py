"""
Base settings that should be standard to all deployments
"""

INSTALLED_APPS = [
    # Adventure apps
    'adventure.core',
    'adventure.magic',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django Addons
    'rest_framework',

]
