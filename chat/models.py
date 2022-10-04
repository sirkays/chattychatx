from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class ChatRoom(models.Model):
    room = models.CharField(max_length=200,blank=True,null=True)
    user_agent_one = models.CharField(max_length=1, default="0")
    user_one = models.CharField(max_length=100, blank=True, null=True)
    user_agent_two = models.CharField(max_length=1, default="1")
    user_two = models.CharField(max_length=100,default="nil")

    @classmethod
    def send_user_agent(cls,agent,room):
        user_one = cls.objects.filter(user_one=agent, room=room)
        user_two = cls.objects.filter(user_two=agent, room=room)
        if len(user_one) == 1:
            return user_one[0].user_agent_one
        elif len(user_two) == 1:
            return user_two[0].user_agent_two
        else:
            if not user_one:
                obj= cls.objects.create(user_one=agent, room=room)
                return obj.user_agent_one
            elif not user_two:
                try:
                    obj= cls.objects.get(room=room)
                    obj.user_two = agent
                    obj.save()
                    return obj.user_agent_two
                except:
                    pass
        return False
        
    def __str__(self):
        return self.room

