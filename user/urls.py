
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('user_profile/<str:username>/', views.user_profile, name='user_profile'),
]