from django.core.exceptions import ObjectDoesNotExist
from django.db import models

class ChatRoom(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
