import os
from celery import Celery

app = Celery(
    "converter",
    broker=os.getenv("CELERY_BROKER_URL", None),
    include=["converter.tasks"],
)

if __name__ == "__main__":
    app.start()
