from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models import Lookup


class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    board = models.ForeignKey(
        LookupValues,
        limit_choices_to={'category_id': 1},
        on_delete=models.RESTRICT)

