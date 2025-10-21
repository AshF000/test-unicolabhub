from django.urls import path
from . import views

app_name = 'collaboration'

urlpatterns = [
    path("add_resource/", views.add_resource, name="add_resource"),
]
