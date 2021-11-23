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
    def get_university_by_id(university_id):
        # gets the relevant university that match the given ID
        return University.objects.get(university_id=university_id)
