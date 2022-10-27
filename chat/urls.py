# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('try/', views.try_now, name='try'),
    path('get_chats/<str:user>/', views.get_chats, name='get_chats'),
    path('<str:room>/<str:current_user>/', views.room, name='room'),
    path('chat_user/<str:room>/<str:current_user>/', views.chat_user, name='chat_user'),
    
]
