from djangostudy.models import CommonModel
from django.db import models

from cafe.models import Cafe

from member.models import Member


class Comment(CommonModel):

    comment_index = models.AutoField(primary_key=True, verbose_name="Comment Index")
    comment_depth = models.IntegerField(blank=True, null=True, verbose_name="depth")
    contents = models.CharField(max_length=24, blank=True, null=True, verbose_name="내용")
    user_index = models.ForeignKey(
        Member,
        on_delete=models.DO_NOTHING,
        verbose_name="member참조아이디",
        db_column="user_index",
        related_name="user_relate2",
        null=True,
    )
    cafe_index = models.ForeignKey(
        Cafe,
        on_delete=models.DO_NOTHING,
        verbose_name="cafe참조아이디",
        db_column="cafe_index",
        related_name="cafe_relate",
        null=True,
    )

    class Meta:
        managed = True
        db_table = "study_comment"
        verbose_name = "댓글"
        app_label = "comment"
