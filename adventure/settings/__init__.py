"""Settings for the project"""
import os

from split_settings.tools import include


include(f'environments/{os.environ.get("DJANGO_ENV", "local")}.py')
