from django.db import models
from django.conf import settings


class DEGREECHOICES(models.TextChoices):
    Computer_Science = 'CS', 'Computer Science'
    Psychology = 'PS', 'Psychology'
    GOVERNMENT = 'GV', 'GOVERNMENT'
    Business_Administration = 'BA', 'Business Administration'
    Unknown = 'UN', 'Unknown'


class TYPECHOICES(models.TextChoices):
    Student = 'S', 'Student'
    Expert = 'E', 'Expert'


class UNIVERSITYCHOICES(models.TextChoices):
    Reichman_University = 'RU', 'Reichman University'
    Hebrew_University = 'HU', 'Hebrew University'
    Tel_Aviv_University = 'TA', 'Tel Aviv University'
    Beer_Sheva_University = 'BS', "Be'er Sheva University"
    Unknown = 'UN', 'Unknown'


class Users(models.Model):
    ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    Name = models.CharField(max_length=30)
    Type = models.CharField(max_length=1, choices=TYPECHOICES.choices, default=TYPECHOICES.Student)
    University = models.CharField(max_length=2, choices=UNIVERSITYCHOICES.choices, default=UNIVERSITYCHOICES.Unknown)
    Degree = models.CharField(max_length=2, choices=DEGREECHOICES.choices, default=DEGREECHOICES.Unknown)
