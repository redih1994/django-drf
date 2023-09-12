import os

from celery import Celery
from django.conf import settings

# TODO: needs to be changed in production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.local")

app = Celery("authors_api")

app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)