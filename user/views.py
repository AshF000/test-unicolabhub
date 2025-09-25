from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Optional: Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register_user')

        # Create the user
        user = User.objects.create_user(username=username, password=password)
        user.is_staff = False  # Cannot access admin
        user.is_superuser = False  # Definitely not admin
        user.save()

        return redirect('user:login_user')

        # # Log the user in
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home')  # Replace 'home' with your landing page name

    return render(request, 'user/register_form.html')  # Show registration form

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
    else:
        return render(request, "user/login_form.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def user_profile(request,username):
    user = User.objects.get(username=username)
    return render(request, 'user/user_profile.html', {'user': user})
