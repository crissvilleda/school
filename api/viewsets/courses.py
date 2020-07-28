"""Course ViewSets"""

# rest_framework
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# models
from api.models import Course
# permission
from api.permissions.users import IsUserAdmin
from api.serializers.courses import AssignSerializer
# Serializer
from api.serializers.courses import CoursesModelSerializer
from api.serializers.scores import AddScoreSerializer, ScoreModelSerializer


class CourseModelViewSet(ModelViewSet):
    """Course ViewSets"""
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CoursesModelSerializer
    lookup_field = 'slug_name'

    def get_permissions(self):
        """handle all permission"""
        permissions = [IsAuthenticated]
        if self.action in ['create', 'update', 'partial_update',
                           'destroy', 'assign', 'add_score']:
            permissions.append(IsUserAdmin)
        return [permission() for permission in permissions]

    def destroy(self, request, *args, **kwargs):
        """rewrite the functions, instead of destroy
            we will set Course.is_active = False.
        """
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def assign(self, request, *args, **kwargs):
        """This functions allow to assign students into de course
            only the administrator user can do it
        """
        data = request.data
        data['course_name'] = kwargs['slug_name']
        serializer = AssignSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        data = {'student': student.get_full_name,
                'message': 'Congratulations, The student has been successfully assigned'
                }
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def add_score(self, request, *args, **kwargs):
        """its function handles the request to add score to a student's test"""
        data = request.data
        data['course_name'] = kwargs['slug_name']
        serializer = AddScoreSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        score = serializer.save()
        data = ScoreModelSerializer(score).data
        data['message'] = 'Score has been successfully assigned'
        return Response(data=data, status=status.HTTP_201_CREATED)
