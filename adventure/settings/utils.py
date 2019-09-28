"""
Base settings that should be standard to all deployments
"""

import inspect
import sys

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

class SettingsLoader:
    """Class-based settings wrapper sourced from readthedocs."""

    @classmethod
    def load_settings(cls, module_name):
        """
        Hoist class & instance variables to the module namespace. Only does this
        for variables that are all upper case and don't start with '_'.

        :params [str] module_name: namespace to target, often '__name__'
        :return: None
        :rtype: None
        """

        self = cls()
        module = sys.modules[module_name]
        for (member, value) in inspect.getmembers(self):
            if member.isupper() and not member.startswith('_'):
                if isinstance(value, property):
                    value = value.fget(self)
                setattr(module, member, value)
