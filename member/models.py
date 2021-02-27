from django.db import models


class Member(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name="유저 아이디")
    user_grant = models.CharField(max_length=20, verbose_name="유저 권한")
    user_name = models.CharField(max_length=24, blank=True, null=True, verbose_name="유저 이름")
    user_age = models.DateTimeField(blank=True, null=True, verbose_name="유저 이름")
    user_email = models.CharField(max_length=20, blank=True, null=True, verbose_name="유저 나이")
    update_date = models.DateTimeField(blank=True, null=True, verbose_name="유저 정보 업데이트일")
    create_date = models.DateTimeField(blank=True, null=True, verbose_name="유저 생성일")
    del_yn = models.CharField(max_length=24, blank=True, null=True, verbose_name="삭제여부")

    class Meta:
        managed = True
        db_table = "study_member"
        verbose_name = "유저"
        app_label = "member"
