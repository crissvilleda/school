"""Students ViewSet"""

# rest_framework
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# models
from api.models import Student
# Custom permission
from api.permissions.users import IsTeacherInCharge
# serializer
from api.serializers import StudentModelSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    """Student Viewset"""
    queryset = Student.objects.filter(is_active=True)
    serializer_class = StudentModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """handle all permission"""
        permissions = [IsAuthenticated]
        if self.action in ['create','update','partial_update','destroy']:
            permissions.append(IsTeacherInCharge)
        return [permission() for permission in permissions]

    def destroy(self, request, *args, **kwargs):
        """rewrite the functions, instead of destroy
        we will set user.is_active = False.
        """
        instance = self.get_object()
        instance.is_active=False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

