"""Admin module"""
# Django
from django.contrib import admin

# models
from api.models import User, Grade, Course, Student, Score


class UserAdmin(admin.ModelAdmin):
    """User Class in admin site"""
    fields = ('username', 'first_name', 'last_name', 'email', 'is_admin', 'is_verify')
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_admin', 'is_verify')
    list_filter = ('is_active', 'is_admin', 'is_verify')
    search_fields = ('username', 'first_name', 'last_name')


class GradeAdmin(admin.ModelAdmin):
    """Grade Class in admin site"""
    fields = ('name', 'in_charge')
    list_display = ('name', 'in_charge')
    search_fields = ('name', 'in_charge')


class CourseAdmin(admin.ModelAdmin):
    """Course Class in admin site"""
    fields = ('slug_name', 'name', 'description', 'is_limited',
              'student_limit', 'teacher', 'grade', 'schedule', 'students')
    list_display = ('name', 'grade', 'teacher', 'schedule')
    search_fields = ('slug_name', 'name', 'description','teacher__first_name')
    list_filter = ('is_limited', 'is_active', 'schedule')


class StudentAdmin(admin.ModelAdmin):
    """Student Class in admin site"""
    fields = ('username', 'first_name', 'last_name', 'parents','grade', 'annotations')
    list_display = ('username', 'first_name', 'last_name', 'parents', 'is_assigned','grade')
    search_fields = ('username', 'first_name', 'last_name', 'parents')
    list_filter = ('is_assigned', 'is_active')


class ScoreAdmin(admin.ModelAdmin):
    """Score Class in admin site"""
    fields = ('student', 'course', 'test_score', 'observations')
    list_display = ('student', 'course', 'test_score', 'observations')
    search_fields = ('student__username','course__name')


admin.site.register(User, UserAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Score, ScoreAdmin)
