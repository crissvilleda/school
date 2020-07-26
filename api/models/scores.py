"""Score Model"""

# Django
from django.db import models

# Utilities
from api.models.utilities import UtilitiesModel


class Score(UtilitiesModel):
    student = models.ForeignKey('api.Student',
                                on_delete=models.CASCADE,
                                related_name='scores'
                                )
    course = models.ForeignKey('api.Course',
                               on_delete=models.CASCADE,
                               related_name='get_scores'
                               )
    score_number = models.FloatField()
    observations = models.TextField(blank=True, null=True)
