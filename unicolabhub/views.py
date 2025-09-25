from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('home')
    else:
        return render(request, "home.html")
