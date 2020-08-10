import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'printer.settings')

app = Celery('printer')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
