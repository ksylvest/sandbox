import os

from celery import Celery  # type: ignore

BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")

celery = Celery(__name__, broker=BROKER_URL, broker_connection_retry_on_startup=True)
