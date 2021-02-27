from django.db import models

from member.models import Member


class Cafe(models.Model):

    cafe_index = models.AutoField(primary_key=True, verbose_name="카페 아이디")
    user_index = models.ForeignKey(Member, on_delete=models.DO_NOTHING, verbose_name="member참조아이디")
    cafe_name = models.CharField(max_length=24, blank=True, null=True, verbose_name="카페 이름")
    update_date = models.DateTimeField(blank=True, null=True, verbose_name="수정 이력")
    create_date = models.DateTimeField(blank=True, null=True, verbose_name="개설 날짜")
    del_yn = models.CharField(max_length=24, blank=True, null=True, verbose_name="삭제여부")

    class Meta:
        managed = True
        db_table = "study_cafe"
        verbose_name = "카페"
        app_label = "cafe"
