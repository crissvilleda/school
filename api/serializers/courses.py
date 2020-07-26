"""Courses Serializer"""

# rest_framework
from rest_framework import serializers

# Model
from api.models import Course


class CoursesModelSerializer(serializers.ModelSerializer):
    """Course model serialzier"""

    class Meta:
        """Meta Courses"""
        model = Course
        fields = [
            'slug_name', 'name', 'description',
            'is_limit', 'student_limit', 'teacher',
            'grade', 'schedule'
        ]
