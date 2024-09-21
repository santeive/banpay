"""
Base user model
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ADMIN = 'admin'
    FILMS = 'films'
    PEOPLE = 'people'
    LOCATIONS = 'locations'
    SPECIES = 'species'
    VEHICLES = 'vehicles'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (FILMS, 'Films'),
        (PEOPLE, 'People'),
        (LOCATIONS, 'Locations'),
        (SPECIES, 'Species'),
        (VEHICLES, 'Vehicles'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

    def __str__(self):
        return self.email
