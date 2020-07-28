"""Utilities Model"""

# Django
from django.db import models


class UtilitiesModel(models.Model):
    """Utilities class
        This Class save the time the every objects was created or edited
    """
    created = models.DateTimeField(
        'Created at',
        auto_now_add=True
    )
    modified = models.DateTimeField(
        'Modified at',
        auto_now=True
    )

    class Meta:
        abstract = True
