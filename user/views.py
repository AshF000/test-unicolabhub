from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def user_profile(request,username):
    user = User.objects.get(username=username)
    return render(request, 'user/user_profile.html', {'user': user})
