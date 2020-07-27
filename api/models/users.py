"""Users model"""
# django
from django.contrib.auth.models import AbstractUser
from django.db import models

# Utilities
from api.models.utilities import UtilitiesModel


class User(AbstractUser, UtilitiesModel):
    """User class
    Used the AbstractUser as it's base and Utilities
    extend the functionality.
    """
    email = models.CharField(max_length=50,
                             unique=True,
                             error_messages={
                                 'unique': 'A user with that email already exists.'
                             }
                             )
    is_admin = models.BooleanField(default=False)
    is_verify = models.BooleanField(
        default=False,
        help_text='Set to true when the user have verified its email address'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
