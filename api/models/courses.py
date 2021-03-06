"""Course Model"""
# Django
from django.db import models

# utilities
from api.models.utilities import UtilitiesModel


class Course(UtilitiesModel):
    """Course class"""
    slug_name = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250,
                                   null=True)
    is_limited = models.BooleanField(default=False)
    student_limit = models.PositiveIntegerField(default=0)
    teacher = models.ForeignKey('api.User',
                                on_delete=models.CASCADE,
                                related_name='get_courses'
                                )
    grade = models.ForeignKey('api.Grade',
                              on_delete=models.CASCADE,
                              related_name='courses')
    students = models.ManyToManyField('api.Student',
                                      related_name='courses',
                                      )
    schedule = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
