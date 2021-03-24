from celery import Celery
from celery.utils.log import get_task_logger
import os
from celery import Celery
from celery.schedules import crontab

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangostudy.initialize.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangostudy.initialize.settings")
app = Celery("djangostudy")

logger = get_task_logger(__name__)


# 문자열로 등록은 Celery Worker가 자식 프로세스에게 피클링하지 하지 않아도 되다고 알림
# namespace = 'CELERY'는 Celery관련 세팅 파일에서 변수 Prefix가 CELERY_ 라고 알림
# >>> celery.config_from_object('myapp.celeryconfig')

# >>> from myapp import celeryconfig
# >>> celery.config_from_object(celeryconfig)


app.config_from_object("django.conf:settings", namespace="CELERY")

# app.config_from_object("djangostudy.initialize.settings", namespace="CELERY")
# app.config_from_object("DJANGO_SETTINGS_MODULE", namespace="CELERY")


# app.autodiscover_tasks(['member'])
app.autodiscover_tasks()


# app = Celery("djangostudy")
#app = Celery()



@app.task(bind=True)
def debug_task(self):
    logger.info("Task executed.")

    print("Request: {0!r}".format(self.request))