from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings

# from django.contrib.auth.models import User


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
    # The AUTH_USER_MODEL is the built in user model from django
    # Goto: https://docs.djangoproject.com/en/3.2/ref/contrib/auth/ for API
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    # name = models.CharField(max_length=30, default="")  # we got the name\username from the built in user model django
    type = models.CharField(max_length=1, choices=TYPECHOICES.choices, default=TYPECHOICES.Student)
    university = models.CharField(max_length=2, choices=UNIVERSITYCHOICES.choices, default=UNIVERSITYCHOICES.Unknown)
    degree = models.CharField(max_length=2, choices=DEGREECHOICES.choices, default=DEGREECHOICES.Unknown)

    # def __str__(self):
    #    return self.user.username


class MessageBoards(models.Model):
    messageBoard_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    courseName = models.CharField(max_length=30)
    # rate = models.CharField(max_length=1, choices=range(1-5), default=3) // we have rate in course class


class Messages(models.Model):
    message_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    messageBoard = models.ForeignKey(MessageBoards, on_delete=models.RESTRICT, related_name='%(class)s_Forum')
    users = models.ForeignKey(Users, on_delete=models.RESTRICT, related_name='%(class)s_author')
    msgDate = models.DateField()
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='%(class)s_tag')


class MessageTags(models.Model):
    messageTags_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    message = models.ForeignKey(Messages, on_delete=models.RESTRICT, related_name='%(class)s_tag')
    users = models.ForeignKey(Users, on_delete=models.RESTRICT, related_name='%(class)s_author')


class University(models.Model):
    university_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=300)  # maybe change here to: description = models.TextField()

    def __str__(self):
        return self.name


class Professor(models.Model):
    professor_id = models.IntegerField(primary_key=True, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.RESTRICT)  # , related_name='%(class)s_something')
    description = models.CharField(max_length=300)  # maybe change here to: description = models.TextField()
    rate = models.CharField(min_length=1, max_length=5, choices=range(1 - 5), default=3)

    def __str__(self):
        return self.name


class Degree(models.Model):
    Degree_id = models.IntegerField(primary_key=True,
                                    validators=[MinValueValidator(0)])
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.RESTRICT)  # , related_name='%(class)s_tag')
    description = models.CharField(max_length=300)  # maybe change here to: description = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True,
                                    validators=[MinValueValidator(0)])  # course id number as given by college?
    name = models.CharField(max_length=100)  # course name as given by college
    rate = models.CharField(min_length=1, max_length=5, choices=range(1 - 5), default=3)
    professor = models.ForeignKey(Professor, on_delete=models.RESTRICT)  # , related_name='%(class)s_something')
    degree = models.ForeignKey(Degree, on_delete=models.RESTRICT)  # , related_name='%(class)s_something')
    description = models.CharField(max_length=300)  # maybe change here to: description = models.TextField()

    def __str__(self):
        return self.name
