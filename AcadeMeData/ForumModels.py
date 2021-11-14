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


class MessageBoards(models.Model):
    ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    CourseName = models.CharField(max_length=30)
    Rate = models.CharField(max_length=1, choices=range(1-5), default=3)


class Messages(models.Model):
    ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    MessageBoard = models.ForeignKey(MessageBoards, on_delete=models.RESTRICT, related_name='%(class)s_Forum')
    Users = models.ForeignKey(Users, on_delete=models.RESTRICT, related_name='%(class)s_author')
    MsgDate = models.DateField()
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='%(class)s_tag')


class MessageTags(models.Model):
    ID = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    Message = models.ForeignKey(Messages, on_delete=models.RESTRICT, related_name='%(class)s_tag')
    Users = models.ForeignKey(Users, on_delete=models.RESTRICT, related_name='%(class)s_author')
