from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    user = request.user
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "home.html", {"user": user})
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "home.html", {"user": user})
    else:
        return render(request, "home.html", {"user": user})
