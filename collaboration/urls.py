from django.urls import path
from . import views

app_name = 'collaboration'

urlpatterns = [
    path("add_resource/", views.add_resource, name="add_resource"),
    path('resource/<int:pk>/', views.view_resource, name='view_resource'),
    path('resource/<int:pk>/edit/', views.edit_resource, name='edit_resource'),
    path('resource/<int:pk>/delete_confirmation/', views.delete_resource, name='delete_resource'),
    path('resource/<int:pk>/delete/', views.confirm_delete, name='confirm_delete'),

]
