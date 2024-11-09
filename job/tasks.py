from __future__ import absolute_import,unicode_literals

from django.http import HttpResponse
from celery import shared_task
from celery.utils.log import get_task_logger

logger=get_task_logger(__name__)

# @shared_task
