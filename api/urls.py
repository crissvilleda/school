"""Urls for the api"""

# rest_framework
from rest_framework.routers import DefaultRouter

from api.viewsets.courses import CourseModelViewSet
# viewsets
from api.viewsets.students import StudentModelViewset
from api.viewsets.users import UserViewset
from api.viewsets.reports import ReportsViewset

router = DefaultRouter()
router.register(r'users', viewset=UserViewset, basename='user')
router.register(r'students', viewset=StudentModelViewset, basename='student')

router.register((r'courses'), viewset=CourseModelViewSet, basename='course')
router.register(r'reports', viewset=ReportsViewset, basename='report')

urlpatterns = router.urls
