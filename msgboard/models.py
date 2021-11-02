from django.db import models
from django.utils import timezone

# Create your models here.


class Message(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
