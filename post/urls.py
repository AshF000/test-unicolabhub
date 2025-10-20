from django.urls import path
from .views import create_event, create_project,create_thesis, view_event, view_thesis, view_project, delete_event, delete_project, delete_thesis, edit_project, edit_event, edit_thesis

app_name = 'post'

urlpatterns = [
    path("create_event/", create_event, name="create_event"),
    path("create_project/", create_project, name="create_project"),
    path("create_thesis/", create_thesis, name="create_thesis"),
    path("view_event/<str:pk>", view_event, name="view_event"),
    path("view_project/<str:pk>", view_project, name="view_project"),
    path("view_thesis/<str:pk>", view_thesis, name="view_thesis"),
    path("delete_event/<str:pk>", delete_event, name="delete_event"),
    path("delete_project/<str:pk>", delete_project, name="delete_project"),
    path("delete_thesis/<str:pk>", delete_thesis, name="delete_thesis"),
    path("edit_event/<str:pk>", edit_event, name="edit_event"),
    path("edit_project/<str:pk>", edit_project, name="edit_project"),
    path("edit_thesis/<str:pk>", edit_thesis, name="edit_thesis"),
]