from django.db import models
from .enum import DELETE


class CommonModel(models.Model):

    del_yn = models.CharField(
        choices=DELETE, default="Y", max_length=24, blank=True, null=True, verbose_name="삭제여부"
    )
    update_date = models.DateTimeField(blank=True, null=True, verbose_name="업데이트일")
    create_date = models.DateTimeField(blank=True, null=True, verbose_name="생성일")

    class Meta:
        abstract = True
