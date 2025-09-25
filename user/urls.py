
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from . import views


urlpatterns = [
    path('logout/', views.logout_user, name='logout_user'),
    path('user_profile/<str:username>/', views.user_profile, name='user_profile'),
]