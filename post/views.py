from django.shortcuts import render, redirect
from .forms import ProjectForm,EventForm,ThesisForm
from .models import Project,Event,Thesis
from collaboration.models import Collaborator

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            collaborator = Collaborator(user=request.user, post=None)
            collaborator.save()
            event.organizer = collaborator
            event.save()
            collaborator.post = event
            collaborator.save()
            return redirect("home")
    else:
        form = EventForm()
    return render(request,'post/create_event.html',{"form":form})

def create_thesis(request):
    if request.method == "POST":
        form = ThesisForm(request.POST)
        if form.is_valid():
            thesis = form.save(commit=False)
            collaborator = Collaborator(user=request.user, post=None)
            collaborator.save()
            thesis.organizer = collaborator
            thesis.save()
            collaborator.post = thesis
            collaborator.save()
            return redirect("home")
    else:
        form = ThesisForm()
    return render(request,'post/create_thesis.html',{"form":form})

def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            collaborator = Collaborator(user=request.user, post=None)
            collaborator.save()
            project.organizer = collaborator
            project.save()
            collaborator.post = project
            collaborator.save()
            return redirect("home")

    else:
        form = ProjectForm()

    return render(request,'post/create_project.html',{"form":form})
