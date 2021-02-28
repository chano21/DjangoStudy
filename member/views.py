from rest_framework.views import APIView

from django.http import Http404, HttpResponse

from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

from drf_yasg.openapi import Parameter
from drf_yasg.openapi import IN_HEADER, TYPE_STRING

# from drf_yasg.openapi import Response as sr


from .models import Member
from .serializers import MemberSerializer


class MemberList(APIView):
    queryset = Member.objects

    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        methods=["get"],
        manual_parameters=[Parameter("Member_Header", IN_HEADER, description="Member Header Test", type=TYPE_STRING)],
    )
    @action(detail=False, methods=["get"], url_path="list")
    def get(self, request, format=None):
        """
        Member List 조회

        """

        queryset = self.queryset

        serializer = MemberSerializer(queryset, many=True)

        return Response(serializer.data, HttpResponse.status_code)


class MemberOne(APIView):
    queryset = Member.objects

    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        methods=["post"],
        request_body=MemberSerializer,
        manual_parameters=[Parameter("member_name", IN_HEADER, type=TYPE_STRING)],
    )
    @action(detail=False, methods=["post"], url_path="")
    def post(self, request, pk=None):

        """

        Member 생성

        """
        print(request.data)
        print(request)
        member_name = request.data["user_name"]
        print(member_name)

        data = Member(
            user_name=request.data.user_name,
            user_grant=request.data.user_grant,
            user_age=request.data.user_age,
            user_email=request.data.user_email,
        )
        data.save()

        # queryset = self.queryset.create

        #  data = request.put
        #  login_user = data.get

        #   user_id = models.AutoField(primary_key=True, verbose_name="유저 아이디")
        #     user_grant = models.CharField(
        #         choices=MEMBER_GRANT, default="Admin", max_length=20, verbose_name="유저 권한", null=False
        #     )
        #     user_name = models.CharField(max_length=24, blank=True, null=True, verbose_name="유저 이름")
        #     user_age = models.DateTimeField(blank=True, null=True, verbose_name="유저 이름")
        #     user_email = models.CharField(max_length=20, blank=True, null=True, verbose_name="유저 나이")

        # data = Member(user_grant=login_user,note_data=note_data.get('note_data'),
        # created_at=datetime.datetime.now(),updated_at=datetime.datetime.now()) data.save()

        #  serializer = MemberSerializer(queryset, many=True)

        return Response(HttpResponse.status_code)