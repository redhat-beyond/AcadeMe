from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings

class University(models.Model):
    university_id = models.IntegerField(
        primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # maybe change here to: description = models.TextField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name
