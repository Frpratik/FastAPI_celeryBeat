from celery import Celery
from celery.signals import after_setup_logger
from .logger import logger
import logging


celery = Celery(
    "news_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["app.tasks"] 
)

celery.conf.beat_schedule = {
    "fetch-news-every-minute": {
        "task": "app.tasks.fetch_news",
        "schedule": 60.0,  
    }
}
celery.conf.timezone = "UTC"

celery_log = logging.getLogger("celery")
celery_log.handlers = logger.handlers
celery_log.setLevel(logger.level)
