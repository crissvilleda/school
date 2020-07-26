"""Urls for the api"""

# rest_framework
from rest_framework.routers import DefaultRouter

from api.viewsets.courses import CourseModelViewSet
# viewsets
from api.viewsets.students import StudentModelViewSet
from api.viewsets.users import UserViewsets

router = DefaultRouter()
router.register(r'users', viewset=UserViewsets, basename='user')
router.register(r'students', viewset=StudentModelViewSet, basename='student')

router.register((r'courses'), viewset=CourseModelViewSet, basename='course')

urlpatterns = router.urls
