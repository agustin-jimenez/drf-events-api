from __future__ import absolute_import, unicode_literals

from celery import Celery
from django.conf import settings

app = Celery('events')
app.conf.timezone = settings.TIME_ZONE
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf['worker_prefetch_multiplier'] = 1
app.conf.update(
    BROKER_URL = 'redis://0.0.0.0:6379/0',
)
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
