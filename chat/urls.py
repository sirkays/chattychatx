# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<str:room>/<str:current_user>/<str:my_image>/<str:other_image>/', views.room, name='room'),
    
]
