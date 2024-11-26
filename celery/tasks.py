import os
from celery import Celery

app = Celery("celery", broker=os.getenv("CELERY_BROKER_URL", None))


@app.task
def add(x, y):
    print(f"ADDING {x} and {y}")
    return x + y
