from django.contrib import admin
from chat import models
admin.site.register(models.ChatBoxData)
admin.site.register(models.Chat)