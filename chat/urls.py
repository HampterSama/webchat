from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('h', views.h, name='h'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]