import os
from celery import Celery

app = Celery("celery", broker=os.getenv("CELERY_BROKER_URL", None))

app.autodiscover_tasks()
