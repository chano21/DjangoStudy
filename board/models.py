from djangostudy.models import CommonModel

from django.db import models
from member.models import Member


class Board(CommonModel):

    board_index = models.AutoField(primary_key=True, verbose_name="게시판 아이디")
    user_index = models.ForeignKey(
        Member,
        on_delete=models.DO_NOTHING,
        verbose_name="member참조아이디",
        db_column="user_index",
        related_name="board_order",
    )
    board_name = models.CharField(max_length=24, blank=True, null=True, verbose_name="게시판 이름")

    class Meta:
        managed = True
        db_table = "study_board"
        verbose_name = "게시판"
        app_label = "board"
