from __future__ import absolute_import
import os
import logging

from celery import Celery
from celery.utils.log import get_task_logger

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
from django.conf import settings

import celery

task_logger = get_task_logger(__name__)
logger = logging.getLogger(__name__)

app = Celery("backend")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def heartbeat(self):
    """make sure beat is running"""
    task_logger.info("[heartbeat] (task logger) {}".format(self.request.id))
    logger.info("[heartbeat] (logger) {}".format(self.request.id))
