# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room>/<str:current_user>/', views.room, name='room'),
    
]
