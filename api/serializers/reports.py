"""Serializer Reports"""

from rest_framework import serializers


class CoursesReportSerializer(serializers.Serializer):
    """Course Report Serializer"""
    name = serializers.StringRelatedField(read_only=True)
    students_count = serializers.IntegerField(read_only=True)
    scores_avg = serializers.FloatField(read_only=True)


class StudentsReportSerializer(serializers.Serializer):
    """Students Report Serializer"""

    student = serializers.SerializerMethodField(read_only=True, source='username')
    scores_avg = serializers.FloatField(read_only=True)

    def get_student(self, instance):
        data = f'{instance.first_name} {instance.last_name}'
        return data
