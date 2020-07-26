"""Students Serializer"""

# rest_framework
from rest_framework import serializers

# Model
from api.models import Student


class StudentModelSerializer(serializers.ModelSerializer):
    """Student Serializer"""

    class Meta:
        """Met class Student"""
        model = Student
        fields = ['username', 'first_name', 'last_name', 'grade',
                  'parents', 'annotations']
