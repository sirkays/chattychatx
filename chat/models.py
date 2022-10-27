from django.core.exceptions import ObjectDoesNotExist
from django.db import models

class ChatBoxData(models.Model):
    room = models.CharField(max_length=2500)
    status = models.BooleanField(default=True)
    user1 = models.CharField(max_length=250)
    user2 = models.CharField(max_length=250)
    my_image = models.CharField(max_length=250,default="avatar.png")
    other_image = models.CharField(max_length=250,default="avatar.png")
    
    
    def __str__(self):
        return f'Status: {self.status}, User1: {self.user1} User2: {self.user2}' 
    
    @classmethod
    def create_room(cls,room,user1,user2):
        return cls.objects.create(room=room, user1=user1,user2=user2)

    @classmethod
    def get_room(cls,room):
        try:
            obj= cls.objects.get(room=room)
            return obj
        except ObjectDoesNotExist:
            return False

class Chat(models.Model):
    chat_box = models.ForeignKey(ChatBoxData,on_delete=models.CASCADE,related_name="chats")
    message = models.TextField(default='')
    user = models.CharField(max_length=250,default='')
    timestamp = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
