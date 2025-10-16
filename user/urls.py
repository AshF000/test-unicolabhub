
from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('update_profile/', views.update_user, name='update_profile'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('update_profile_pic/', views.update_profile_pic, name='update_profile_pic'),
]