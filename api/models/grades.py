"""Grade Model"""

# django
from django.db import models

# Utilities
from api.models.utilities import UtilitiesModel


class Grade(UtilitiesModel):
    """Grade Class"""
    name = models.CharField(max_length=150,
                            unique=True
                            )
    in_charge = models.OneToOneField('api.User',
                                     on_delete=models.CASCADE,
                                     related_name='grade',
                                     blank=True, null=True)

    def __str__(self):
        return self.name
