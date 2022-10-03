from django.core.exceptions import ObjectDoesNotExist
from django.db import models

class ChatRoom(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

    @classmethod
    def get_room(cls,room,mode=True):
        try:
            return cls.objects.get(title=room)
        except ObjectDoesNotExist:
            if mode:
                return cls.objects.create(title=room)
            return False