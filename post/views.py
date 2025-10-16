from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime

from .forms import ProjectForm, EventForm, ThesisForm
from .models import Project, Event, Thesis
from collaboration.models import Collaborator


def create_event(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        status = request.POST.get('status')

        cover_pic = request.FILES.get('cover_pic')
        schedule = request.FILES.get('schedule')

        start_time = parse_datetime(request.POST.get('start_time'))
        end_time = parse_datetime(request.POST.get('end_time'))

        collaborator = Collaborator(user=request.user, post=None)
        collaborator.save()

        event = Event.objects.create(
            organizer=collaborator,
            title=title,
            description=description,
            location=location,
            status=status,
            start_time=start_time,
            end_time=end_time,
            cover_pic=cover_pic,
            schedule=schedule,
        )

        collaborator.post = event
        collaborator.save()

        return redirect('home')

    return render(request, 'post/create_event.html')


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
    return render(request, 'post/create_thesis.html', {"form": form})


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

    return render(request, 'post/create_project.html', {"form": form})


def view_project(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'post/view_project.html', {"project": project})


def view_thesis(request, pk):
    thesis = Thesis.objects.get(pk=pk)
    return render(request, 'post/view_thesis.html', {"thesis": thesis})


def view_event(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'post/view_event.html', {"event": event})


def edit_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            return redirect("home")
    else:
        form = ProjectForm(instance=project)
    return render(request, 'post/edit_project.html', {"form": form})


def edit_thesis(request, pk):
    thesis = Thesis.objects.get(pk=pk)
    if request.method == "POST":
        form = ThesisForm(request.POST, instance=thesis)
        if form.is_valid():
            thesis = form.save(commit=False)
            return redirect("home")
    else:
        form = ThesisForm(instance=thesis)

    return render(request, 'post/edit_thesis.html', {"form": form})


def edit_event(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            return redirect("home")

    else:
        form = EventForm(instance=event)

    return render(request, 'post/edit_event.html', {"form": form})


def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect("home")
    return render(request, 'post/delete_project.html', {"project": project})


def delete_thesis(request, pk):
    thesis = Thesis.objects.get(pk=pk)
    if request.method == "POST":
        thesis.delete()
        return redirect("home")
    return render(request, 'post/delete_thesis.html', {"thesis": thesis})


def delete_event(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == "POST":
        event.delete()
        return redirect("home")
    return render(request, 'post/delete_event.html', {"event": event})
