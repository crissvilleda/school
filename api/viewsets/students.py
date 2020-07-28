"""Students ViewSet"""

# rest_framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# models
from api.models import Student
# Custom permission
from api.permissions.users import IsTeacherInCharge
# serializer
from api.serializers import StudentModelSerializer
from api.serializers.courses import CourseDetailSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    """Student ViewSets"""
    queryset = Student.objects.filter(is_active=True)
    serializer_class = StudentModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """handle all permission"""
        permissions = [IsAuthenticated]
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions.append(IsTeacherInCharge)
        elif self.action == 'courses':
            permissions.append(AllowAny)
        return [permission() for permission in permissions]

    def destroy(self, request, *args, **kwargs):
        """rewrite the functions, instead of destroy
        we will set user.is_active = False.
        """
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def courses(self, request, *args, **kwargs):
        """this function will get the list of courses the student is into,
            and detail of his/her test score.
        """
        username = kwargs['username']
        # validate if the student exists
        student = get_object_or_404(Student, username=username, is_active=True)
        query = student.courses.all()
        if not query.exits():
            pass
        query = [x for x in query]
        serializer = CourseDetailSerializer(query,
                                            context={'student': student.username},
                                            many=True)
        data = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)
