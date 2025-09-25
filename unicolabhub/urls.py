
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("home/", lambda request: redirect("home")),
    path('user/', include('user.urls')),
]