"""File to configurecelery"""

import os

from celery import Celery


APP = Celery('adventure')
APP.config_from_object('django.conf:settings', namespace='CELERY')
APP.autodiscover_tasks()
