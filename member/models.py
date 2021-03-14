from djangostudy.models import CommonModel
from django.db import models


from djangostudy.enum import MEMBER_GRANT


class Member(CommonModel):

    user_index = models.AutoField(primary_key=True, verbose_name="유저 아이디")
    user_grant = models.CharField(
        choices=MEMBER_GRANT, default="Admin", max_length=20, verbose_name="유저 권한", null=False
    )
    user_name = models.CharField(max_length=24, blank=True, null=True, verbose_name="유저 이름")
    user_age = models.DateTimeField(blank=True, null=True, verbose_name="유저 이름")
    user_email = models.CharField(max_length=20, blank=True, null=True, verbose_name="유저 나이")

    class Meta:
        managed = True
        db_table = "study_member"
        verbose_name = "유저"
        app_label = "member"


class UnionMmeberWithComment(CommonModel):

    col1 = models.CharField(max_length=24, blank=True, null=True, verbose_name="col1")
    col2 = models.CharField(max_length=24, blank=True, null=True, verbose_name="col2")

    class Meta:
        managed = False
        #  db_table = "study_member"
        verbose_name = "유저"
        app_label = "member"
