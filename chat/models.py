from django.core.exceptions import ObjectDoesNotExist
from django.db import models

class ChatBoxData(models.Model):
    room = models.CharField(max_length=2500)
    status = models.BooleanField(default=True)
    user1 = models.CharField(max_length=250)
    user2 = models.CharField(max_length=250)
    
    def __str__(self):
        return f'Status: {self.status}, User1: {self.user1} User2: {self.user2}' 
    
    @classmethod
    def create_room(cls,room,user1,user2):
        if room and user1 and user2:
            return cls.objects.create(room=room, user1=user1,user2=user2)
        return False

    @classmethod
    def get_room(cls,room):
        try:
            return cls.objects.get(room=room)
        except ObjectDoesNotExist:
            return False


