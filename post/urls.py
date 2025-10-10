from django.urls import path
from .views import create_event, create_project,create_thesis

app_name = 'post'

urlpatterns = [
    path("create_event/", create_event, name="create_event"),
    path("create_project/", create_project, name="create_project"),
    path("create_thesis/", create_thesis, name="create_thesis"),
]