from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet, mixins, ModelViewSet

# from rest_framework.views import GenericViewSet,mixins,ListModelMixin
#  mixins.RetrieveModelMixin,
#     mixins.ListModelMixin,
#     GenericViewSet,
from django.http import Http404, HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

from drf_yasg.openapi import Parameter
from drf_yasg.openapi import IN_HEADER, TYPE_STRING

# from drf_yasg.openapi import Response as sr

from django.db.models import OuterRef, Exists, F
from .models import Member
from board.models import Board
from cafe.models import Cafe
from comment.models import Comment

from .serializers import MemberSerializer, UnionSerializer

import os

import time


# class MemberViewSet(ModelViewSet):
class MemberViewSet(mixins.ListModelMixin, GenericViewSet):
    # serializer_class = UnionSerializer

    def get_serializer_class(self):
        pass
        # if self.action == "list":
        #     return UnionSerializer

    """

    Member rounter
    """

    @swagger_auto_schema(
        methods=["get"],
    )
    # @action(detail=False, methods=["get"], url_path="")
    def list(self, request, *args, **kwargs):
        return Response("hello")

    queryset = Member.objects

    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        methods=["get"],
        #     manual_parameters=[Parameter("Member_Header", IN_HEADER, description="Member Header Test", type=TYPE_STRING)],
    )
    @action(detail=False, methods=["get"], url_path="memberlist")
    def memberlist(self, request):

        """
        Member List 조회

        """
        start = time.time()

        valuelist = ("contents", "comment_depth")

        # comment = Comment.objects.annotate(col1=F("contents"), col2=F("comment_depth")).values("col1", "col2")

        comment = Comment.objects.annotate(col1=F("contents"), col2=F("comment_depth")).only(*valuelist)

        print("time :", time.time() - start)
        result = comment.union(comment)
        # serial = self.serializer_class(data=result)
        # serial.is_valid(raise_exception=True)
        # serial.save()
        serializer = UnionSerializer(result, many=True)
        print(f"result: {serializer}")

        return Response(serializer.data)

    @swagger_auto_schema(
        methods=["put"],
        #     manual_parameters=[Parameter("Member_Header", IN_HEADER, description="Member Header Test", type=TYPE_STRING)],
    )
    @action(detail=False, methods=["put"], url_path="membercreate")
    def membersave(self, request):

        """
        Member create

        """

        #       user_index = models.AutoField(primary_key=True, verbose_name="유저 아이디")
        # user_grant = models.CharField(
        #     choices=MEMBER_GRANT, default="Admin", max_length=20, verbose_name="유저 권한", null=False
        # )
        # user_name = models.CharField(max_length=24, blank=True, null=True, verbose_name="유저 이름")
        # user_age = models.DateTimeField(blank=True, null=True, verbose_name="유저 이름")
        # user_email = models.CharField(max_length=20, blank=True, null=True, verbose_name="유저 나이")

        Member.objects.create(user_grant="admin", user_name="create_test_name", user_email="create@mail.com")

        return Response("create_success")


# class MemberList(APIView):
# class MemberList(mixins.ListModelMixin, GenericViewSet):

#     # class MemberList(mixins.ListModelMixin, GenericViewSet):


# class MemberOne(APIView):
#     queryset = Member.objects

#     def get_object(self, pk):
#         try:
#             return Member.objects.get(pk=pk)
#         except Member.DoesNotExist:
#             raise Http404

#     @swagger_auto_schema(
#         methods=["post"],
#         request_body=MemberSerializer,
#         #      manual_parameters=[Parameter("member_name", IN_HEADER, type=TYPE_STRING)],
#     )
#     @action(detail=False, methods=["post"], url_path="")
#     def post(self, request, pk=None):

#         """

#         Member 생성

#         """
#         print(request.data)
#         print(request)
#         member_name = request.data["user_name"]
#         print(member_name)

#         data = Member(
#             user_name=request.data["user_name"],
#             user_grant=request.data["user_grant"],
#             user_age=request.data["user_age"],
#             user_email=request.data["user_email"],
#         )
#         data.save()
#         # queryset = self.queryset.create

#         #  data = request.put
#         #  login_user = data.get

#         #   user_id = models.AutoField(primary_key=True, verbose_name="유저 아이디")
#         #     user_grant = models.CharField(
#         #         choices=MEMBER_GRANT, default="Admin", max_length=20, verbose_name="유저 권한", null=False
#         #     )
#         #     user_name = models.CharField(max_length=24, blank=True, null=True, verbose_name="유저 이름")
#         #     user_age = models.DateTimeField(blank=True, null=True, verbose_name="유저 이름")
#         #     user_email = models.CharField(max_length=20, blank=True, null=True, verbose_name="유저 나이")

#         # data = Member(user_grant=login_user,note_data=note_data.get('note_data'),
#         # created_at=datetime.datetime.now(),updated_at=datetime.datetime.now()) data.save()

#         #  serializer = MemberSerializer(queryset, many=True)

#         return Response(HttpResponse.status_code)