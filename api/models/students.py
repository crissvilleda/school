"""Student Model"""
# Django
from django.db import models

# Utilities
from api.models.utilities import UtilitiesModel


class Student(UtilitiesModel):
    """Student Class"""
    username = models.CharField(max_length=100, unique=True)
    grade = models.ForeignKey('api.Grade', on_delete=models.CASCADE, related_name='get_students')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    parents = models.CharField(max_length=200)
    is_assigned = models.BooleanField(default=False)
    annotations = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
