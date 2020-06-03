import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.conf.broker_url = 'redis://127.0.0.1:6379/0'
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.timezone = 'UTC'
app.conf.beat_schedule = {
  'send-spam-every-5-sec': {
    'task': 'core.tasks.periodic_task',
    'schedule': crontab(minute='*/1')
  }
}