from rest_framework.views import APIView
from django.http import Http404


from rest_framework.response import Response

from .models import Cafe
from .serializers import CafeSerializer


class CafeList(APIView):
    def get_object(self, pk):
        try:
            return Cafe.objects.get(pk=pk)
        except Cafe.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        # queryset = Cafe.objects.all()
        queryset = Cafe.objects.all()

        # cafe = self.get_object()
        serializer = CafeSerializer(queryset, many=True)
        #    print("테스트 : " + str(serializer.data))
        return Response(serializer.data)
