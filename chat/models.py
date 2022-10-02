from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Message(models.Model):
    author = models.CharField(max_length=250)
    context = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)