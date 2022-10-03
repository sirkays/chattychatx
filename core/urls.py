from django.contrib import admin
from django.urls import path, include
from chat.views import set_room
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('set_room/', set_room, name='set_room'),

]
