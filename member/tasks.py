from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task(bind=True)
def test(self, arg):
    print(arg)
    for i in range(1, 10000):
        print(str(i))


# @shared_task
# #@app.task(serializer='json')
# def add(self, x, y):

#     logger.info("Task executed.")
#     logger.debug("Task executed.")
#     print("x + y : " + str(x + y))
#     return x + y
