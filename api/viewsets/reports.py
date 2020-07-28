"""Reports ViewSets"""
# django
from django.db.models import Avg, Count
# rest_framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# models
from api.models import Course, Student
# seraliser
from api.serializers.reports import CoursesReportSerializer, StudentsReportSerializer


class ReportsViewset(viewsets.GenericViewSet):
    """Reports Serializer"""

    @action(detail=False, methods=['get'])
    def courses(self, request):
        """Generate the following reports:
            --Number of registered students per course
            --Average score per course over total students
        """
        query = Course.objects.annotate(students_count=Count('students', distinct=True),
                                        scores_avg=Avg('get_scores__test_score'))

        serializer = CoursesReportSerializer(query, many=True)
        data = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def students(self, request):
        """Generate the following reports:
            --Average score per student in each of their courses
        """
        query = Student.objects.annotate(scores_avg=Avg('scores__test_score'))

        serializer = StudentsReportSerializer(query, many=True)
        data = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)
