"""Serializer Reports"""
# rest_framework
from rest_framework import serializers


class CoursesReportSerializer(serializers.Serializer):
    """Course Report Serializer"""
    name = serializers.StringRelatedField(read_only=True)
    students_count = serializers.SerializerMethodField(read_only=True)
    scores_avg = serializers.SerializerMethodField(read_only=True)

    def get_students_count(self, data):
        """Add value 0 is count is null or None"""
        if data.students_count is None:
            data.students_count = 0
        count = data.students_count
        return count

    def get_scores_avg(self, data):
        """Add value 0 is Average is null or None"""
        if data.scores_avg is None:
            data.scores_avg = 0
        avg = round(data.scores_avg, 2)
        return avg


class StudentsReportSerializer(serializers.Serializer):
    """Students Report Serializer"""

    student = serializers.SerializerMethodField(read_only=True, source='username')
    scores_avg = serializers.SerializerMethodField(read_only=True)

    def get_student(self, data):
        """Add full name to the student attribute"""
        student = f'{data.first_name} {data.last_name}'
        return student

    def get_scores_avg(self, data):
        """Add value 0 if the score is null or None"""
        if data.scores_avg is None:
            data.scores_avg = 0
        score = data.scores_avg
        return score
