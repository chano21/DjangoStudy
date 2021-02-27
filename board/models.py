from django.db import models

from member.models import Member


class board(models.Model):

    board_index = models.AutoField(primary_key=True, verbose_name="게시판 아이디")
    user_index = models.ForeignKey(Member, on_delete=models.DO_NOTHING, verbose_name="member참조아이디")
    #  board_index = models.ForeignKey(primary_key=True, verbose_name="게시판 아이디")
    board_name = models.CharField(max_length=24, blank=True, null=True, verbose_name="게시판 이름")
    update_date = models.DateTimeField(blank=True, null=True, verbose_name="수정 이력")
    create_date = models.DateTimeField(blank=True, null=True, verbose_name="개설 날짜")
    del_yn = models.CharField(max_length=24, blank=True, null=True, verbose_name="삭제여부")

    class Meta:
        managed = True
        db_table = "study_board"
        verbose_name = "게시판"
        app_label = "board"
