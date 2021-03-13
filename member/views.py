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

    serializer_class = UnionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return UnionSerializer

    """

    Member rounter
    """

    # @swagger_auto_schema(
    #     # methods=["get"],
    #     # url_path="pointlist",
    #     manual_parameters=[
    #         openapi.Parameter(
    #             "offset", openapi.IN_QUERY, description="쿼리의 시작 위치(1~30/31~60/...)", type=openapi.TYPE_STRING
    #         ),
    #         openapi.Parameter(
    #             "limit", openapi.IN_QUERY, description="한 페이지에서 보여주는 row 수(default=30)", type=openapi.TYPE_STRING
    #         ),
    #         openapi.Parameter("page", openapi.IN_QUERY, description="현재 페이지", type=openapi.TYPE_STRING),
    #         openapi.Parameter("created_at_lte", openapi.IN_QUERY, description="Before 기간", type=openapi.TYPE_STRING),
    #         openapi.Parameter("created_at_gte", openapi.IN_QUERY, description="After 기간", type=openapi.TYPE_STRING),

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

#        self.serializers = UnionSerializer

        #   testquery = self.filter_queryset()
        """
        Member List 조회

        """
        # print("now pid : " + str(os.getpid()))

        # queryset1 = Board.objects.select_related("user_index")
        # print(f"{queryset1}")
        # queryset1 = Board.objects.prefetch_related("user_index")
        # print(f"{queryset1}")
        start = time.time()
        comment = Comment.objects.annotate(col1=F("contents"), col2=F("comment_depth")).values("col1", "col2")
        member = Member.objects.annotate(col1=F("user_name"), col2=F("user_email")).values("col1", "col2")
        print("time :", time.time() - start)

        # start = time.time()
        # comment = Comment.objects.annotate(changecolumns1="contents", changecolumns2="cafe_name").values(
        #     "changecolumns1", "changecolumns2"
        # )
        # member = Member.objects.annotate(changecolumns1="user_name", changecolumns2="user_email").values(
        #     "changecolumns1", "changecolumns2"
        # )
        # print("time :", time.time() - start)
        # result = comment.union(member)
        result = comment.union(member)
        serial = self.serializers(result)
        print(f"result: {serial}")

        serialdata = self.get_serializer(serial, many=True)

        print(serialdata)

        # serializer = self.get_serializer(page, many=True)

        # cafe1.get_queryset()
        # cafe2 = Cafe.objects.select_related("user_index")

        # queryset2 = Member.objects.filter(
        #     user_name=["name1", "name2"],
        #     #     user_index=OuterRef("pk"),
        # )

        # queryset3 = Member.objects.all()

        # if not Member.objects.filter(
        #     ~Exists(
        #         Member.objects.filter(
        #             user_name__in=["name1", "name2"],
        #             user_index=OuterRef("pk"),
        #         )
        #     )
        # ).exists():
        #     print("Hi")
        # else:
        #     print("No")

        #  print(f"{queryset3[0]}")
        # Cafe.objects.select_related.('')
        # print(f"{queryset3[0].user_name}")

        # print(f"{queryset3}")

        # serializer = MemberSerializer(cafe1, many=True)
        #   cafe1 = Comment.objects.prefetch_related("user_index").values()
        return Response(result)


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