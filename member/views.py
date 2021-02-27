from rest_framework.views import APIView
from django.http import Http404

from rest_framework.response import Response

from .models import Member
from .serializers import MemberSerializer


class MemberList(APIView):
    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        queryset = Member.objects.all()

        serializer = MemberSerializer(queryset, many=True)

        return Response(serializer.data)
