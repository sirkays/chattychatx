# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<str:room>/<str:current_user>/', views.room, name='room'),
    path('chat_user/<str:room>/<str:current_user>/', views.chat_user, name='chat_user'),
    
]
