"""Score Model"""

# Django
from django.db import models

# Utilities
from api.models.utilities import UtilitiesModel


class Score(UtilitiesModel):
    """Score Class"""
    student = models.ForeignKey('api.Student',
                                on_delete=models.CASCADE,
                                related_name='scores'
                                )
    course = models.ForeignKey('api.Course',
                               on_delete=models.CASCADE,
                               related_name='get_scores'
                               )
    test_score = models.FloatField()
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.test_score}'
