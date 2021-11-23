from django.core.validators import MinValueValidator
from django.db import models


class University(models.Model):
    university_id = models.IntegerField(
        primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # maybe change here to: description = models.TextField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_university_by_name(name):
        # gets the relevant university that match the given name
        return University.objects.get(name=name)
    
    @staticmethod
    def get_university_by_location(location):
        # gets the relevant university that match the given location
        return University.objects.get(location=location)
