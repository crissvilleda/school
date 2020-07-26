"""Utilities Model"""

# Django
from django.db import models


class UtilitiesModel(models.Model):
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
