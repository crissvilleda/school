"""Students Serializer"""

# rest_framework
from rest_framework import serializers

# Model
from api.models import Student


class StudentModelSerializer(serializers.ModelSerializer):
    """Student Serializer"""
    grade_name = serializers.StringRelatedField(source='grade', read_only=True)

    class Meta:
        """Met class Student"""
        model = Student
        fields = ['username', 'first_name', 'last_name', 'grade_name', 'grade',
                  'parents', 'annotations']
        extra_kwargs = {
            'grade': {'write_only': True}
        }
