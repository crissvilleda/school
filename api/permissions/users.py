"""User permission"""

# rest_fremework
from rest_framework.permissions import BasePermission

# Model
from api.models import Grade


class IsUserAdmin(BasePermission):
    """Admin permission"""

    def has_permission(self, request, view):
        """Allow to do actions only if the user is admin"""
        return request.user.is_admin


class IsTeacherInCharge(BasePermission):
    """Allow to add students only if he/she is teacher in charge"""

    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT']:
            data = request.data
        elif request.method in ['PATCH', 'DELETE']:
            data = {
                'grade': view.get_object().grade.pk
            }
        try:
            Grade.objects.get(
                pk=data['grade'],
                in_charge=request.user
            )
        except (Grade.DoesNotExist, KeyError) as Error:
            return False
        return True
