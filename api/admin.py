"""Admin module"""
# Django
from django.contrib import admin

# models
from api.models import User, Grade, Course


class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'first_name', 'last_name', 'email', 'is_admin','is_verify')
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_admin', 'is_verify')
    list_filter = ('is_active', 'is_admin', 'is_verify')
    search_fields = ('username', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)


class GradeAdmin(admin.ModelAdmin):
    fields = ('name', 'in_charge')
    list_display = ('name', 'in_charge')
    search_fields = ('name', 'in_charge')


admin.site.register(Grade, GradeAdmin)


class CourseAdmin(admin.ModelAdmin):
    fields = ('slug_name', 'name', 'description','is_limited',
              'student_limit', 'teacher', 'grade', 'schedule')
    list_display = ('name', 'grade', 'teacher', 'schedule')
    search_fields = ('slug_name', 'name', 'description')
    list_filter = ('is_limited', 'is_active', 'schedule')


admin.site.register(Course, CourseAdmin)
