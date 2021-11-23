from django.db import models
from django.utils import timezone
from django.conf import settings


class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
