"""Course viewset"""

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# rest_framework
from rest_framework.viewsets import ModelViewSet

# models
from api.models import Course
# Serialiser
from api.serializers.courses import CoursesModelSerializer


class CourseModelViewSet(ModelViewSet):
    """Coruse viewset"""
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CoursesModelSerializer
    lookup_field = 'slug_name'

    def get_permissions(self):
        """handle all permission"""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def destroy(self, request, *args, **kwargs):
        """rewrite the functions, instead of destroy
        we will set Course.is_active = False.
        """
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
