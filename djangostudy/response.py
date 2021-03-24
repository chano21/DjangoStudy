from rest_framework.response import Response

# from rest_framework import serializers
from rest_framework import serializers
from collections import OrderedDict


class PCOResponse(Response, serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super(serializers.ModelSerializer, self).to_representation(instance)
        result = OrderedDict()
        result["data"] = data
        result["message"] = "Done"
        result["status"] = "sucssed"
        return result
