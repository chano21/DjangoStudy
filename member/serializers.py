from drf_yasg.openapi import Parameter
from rest_framework import serializers
from .models import Member, UnionMmeberWithComment,MyModel


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class UnionSerializer(serializers.ModelSerializer):
    col1 = serializers.SerializerMethodField()
    col2 = serializers.SerializerMethodField()

    class Meta:
        model = UnionMmeberWithComment
        fields = "__all__"

    #        fields = ("col1", "col2")

    def get_col1(self, obj):
        if obj["col1"] is None:
            return ""
        else:
            return obj["col1"]

    def get_col2(self, obj):
        if obj["col2"] is None:
            return ""
        else:
            return obj["col2"]
            





class MyModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyModel
        fields = ('file','is_active')