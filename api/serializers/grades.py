"""Grade Serializer"""

# rest_framework
from rest_framework import serializers

# model
from api.models import Grade
# serializer
from api.serializers.users import UserModelSerializer


class GradeModelSerializer(serializers.ModelSerializer):
    """Grade Model Serializer"""
    in_charge = UserModelSerializer(read_only=True)

    class Meta:
        """Meta Class"""
        model = Grade
        fields = ('name', 'in_charge')
