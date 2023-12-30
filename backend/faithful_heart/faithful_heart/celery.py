import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faithful_heart.settings')

app = Celery('faithful_heart')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
