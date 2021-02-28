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
    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        methods=["get"],
        manual_parameters=[Parameter("Member_Header", IN_HEADER, description="Member Header Test", type=TYPE_STRING)],
    )
    @action(detail=False, methods=["get"], url_path="member")
    def get(self, request, format=None):
        """
        Member List 조회

        """

        queryset = Member.objects.all()

        serializer = MemberSerializer(queryset, many=True)

        return Response(serializer.data, HttpResponse.status_code)
