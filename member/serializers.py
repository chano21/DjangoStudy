from rest_framework import serializers
from .models import Member, UnionMmeberWithComment


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class UnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnionMmeberWithComment
        fields = "__all__"
