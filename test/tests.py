from django.test import TestCase

from .models import Member
from djangostudy.enum import MEMBER_GRANT, DELETE


class MemberTest(TestCase):

    """ Test module for Puppy model """

    # user_id = models.AutoField(primary_key=True, verbose_name="유저 아이디")
    # user_grant = models.CharField(choices=(("admin", "grant"), ("user", "grant")), max_length=20, verbose_name="유저 권한")
    # user_name = models.CharField(max_length=24, blank=True, null=True, verbose_name="유저 이름")
    # user_age = models.DateTimeField(blank=True, null=True, verbose_name="유저 이름")
    # user_email = models.CharField(max_length=20, blank=True, null=True, verbose_name="유저 나이")
    # update_date = models.DateTimeField(blank=True, null=True, verbose_name="유저 정보 업데이트일")
    # create_date = models.DateTimeField(blank=True, null=True, verbose_name="유저 생성일")
    # del_yn = models.CharField(max_length=24, blank=True, null=True, verbose_name="삭제여부")

    def setUp(self):
        Member.objects.create(
            user_name="test1",
            user_grant=MEMBER_GRANT["Admin"],
            user_age=18,
            user_email="tes@mail.com",
            del_yn=DELETE["N"],
        )
        Member.objects.create(
            user_name="test2",
            user_grant=MEMBER_GRANT["User"],
            user_age=23,
            user_email="tes@mail.com",
            del_yn=DELETE["N"],
        )
        Member.objects.create(
            user_name="test3",
            user_grant=MEMBER_GRANT["Admin"],
            user_age=11,
            user_email="tes@mail.com",
            del_yn=DELETE["N"],
        )

    def test_puppy_breed(self):
        m1 = Member.objects.get(name="test1")
        m2 = Member.objects.get(name="test2")
        print(f"m1={m1}")
        print(f"m2={m2}")

    # print(f"Calling ModelBase's __prepare__ method with name={name} and bases={bases}")
    #  m1.get

    # self.assertEqual(m1.get_.get_breed(), "Casper belongs to Bull Dog breed.")
    # self.assertEqual(puppy_muffin.get_breed(), "Muffin belongs to Gradane breed.")
