from django.urls import path
from .views import create_event, create_project,create_thesis, view_event, view_thesis, view_project

app_name = 'post'

urlpatterns = [
    path("create_event/", create_event, name="create_event"),
    path("create_project/", create_project, name="create_project"),
    path("create_thesis/", create_thesis, name="create_thesis"),
    path("view_event/<str:pk>", view_event, name="view_event"),
    path("view_project/<str:pk>", view_project, name="view_project"),
    path("view_thesis/<str:pk>", view_thesis, name="view_thesis"),
]