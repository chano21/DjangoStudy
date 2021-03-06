from djangostudy.models import CommonModel
from django.db import models


from djangostudy.enum import MEMBER_GRANT


class Member(models.Model):

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


class UnionMmeberWithComment(models.Model):

    col1 = models.CharField(max_length=24, blank=True, null=True, verbose_name="col1")
    col2 = models.CharField(max_length=24, blank=True, null=True, verbose_name="col2")
    custom_index = models.CharField(max_length=24, blank=True, null=True, verbose_name="custom_index")
    dummy_data = models.CharField(max_length=24, blank=True, null=True, verbose_name="dummy_data")

    class Meta:
        managed = False
        #  db_table = "study_member"
        verbose_name = "유저"
        app_label = "member"


class MyModel(models.Model):

    file = models.ImageField(upload_to=u"photos")
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return u"photo {0}".format(self.file.url)