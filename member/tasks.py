from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def add(x, y):
    logger.debug("Task executed.")
    print("x + y : " + str(x + y))
    return x + y
