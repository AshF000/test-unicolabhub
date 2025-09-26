from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import CollabUser
from .forms import UserUpdateForm, CollabUserUpdateForm


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if any field is empty
        # if not username or not password or not confirm_password:
        #     messages.error(request, "All fields are required.")
        #     return redirect('register_user')

        # Check if password and confirm password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('user:register_user')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('user:register_user')

        # Create the user
        user = User.objects.create_user(username=username, password=password)
        user.is_staff = False  # Cannot access admin
        user.is_superuser = False  # Definitely not admin
        user.save()

        # Successful registration message
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('user:login_user')

        # For GET request, render the registration form
    return render(request, 'user/register_form.html')


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
            return render(request, "user/login_form.html")
    else:
        return render(request, "user/login_form.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def user_profile(request):
    user = request.user
    return render(request, 'user/user_profile.html')


@login_required
def update_user(request):
    user = request.user
    profile = CollabUser.objects.get(user=user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = CollabUserUpdateForm(request.POST, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user:user_profile')  # Or wherever you want

    else:
        u_form = UserUpdateForm(instance=user)
        p_form = CollabUserUpdateForm(instance=profile)

    return render(request, 'user/update_profile.html', {
        'u_form': u_form,
        'p_form': p_form
    })

@login_required
def delete_user(request):
    if request.method == "POST":
        password = request.POST.get("password")
        user = request.user

        if user.check_password(password):
            username = user.username

            logout(request)  # log user out before deleting
            user.delete()    # deletes user and cascades CollabUser

            messages.success(request, f"User '{username}' account deleted successfully.")
            return redirect('home')
        else:
            messages.error(request, "Incorrect password. Please try again.")

    return render(request, "user/delete_confirmation.html")