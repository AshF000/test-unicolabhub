from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime, parse_date

from .forms import ProjectForm, EventForm, ThesisForm
from .models import Project, Event, Thesis
from collaboration.models import Collaborator
from user.models import Opinion


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
    else:
        form = EventForm()

    return render(request, 'post/create_event.html', {"form": form})


def create_thesis(request):
    if request.method == "POST":

        title = request.POST.get('title')
        description = request.POST.get('description')
        research_topic = request.POST.get('research_topic')
        research_field = request.POST.get('research_field')

        start_date = parse_date(request.POST.get('start_date'))
        end_date = parse_date(request.POST.get('end_date'))

        status = request.POST.get('status')

        cover_pic = request.FILES.get('cover_pic')

        collaborator = Collaborator(user=request.user, post=None)
        collaborator.save()

        thesis = Thesis.objects.create(
            organizer=collaborator,
            title=title,
            description=description,
            research_topic=research_topic,
            research_field=research_field,

            start_date=start_date,
            end_date=end_date,

            status=status,
            cover_pic=cover_pic,
        )

        collaborator.post = thesis
        collaborator.save()
        return redirect("home")
    else:
        form = ThesisForm()

    return render(request, 'post/create_thesis.html', {"form": form})


def create_project(request):
    if request.method == "POST":

        title = request.POST.get('title')
        description = request.POST.get('description')

        start_date = parse_date(request.POST.get('start_date'))
        deadline = parse_date(request.POST.get('deadline'))

        status = request.POST.get('status')

        cover_pic = request.FILES.get('cover_pic')

        criteria = request.POST.get('criteria')

        collaborator = Collaborator(user=request.user, post=None)
        collaborator.save()

        project = Project.objects.create(
            organizer=collaborator,
            title=title,
            description=description,

            start_date=start_date,
            deadline=deadline,

            status=status,
            cover_pic=cover_pic,

            criteria=criteria,
        )

        collaborator.post = project
        collaborator.save()
        return redirect("home")
    else:
        form = ProjectForm()

    return render(request, 'post/create_project.html', {"form": form})


def view_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == "POST":
        opinion = request.POST.get('opinion')
        Opinion.objects.create(user=request.user, opinion=opinion, post=project)
    opinions = Opinion.objects.all()
    op_fil=[]
    for op in opinions:
        if op.post == project:
            op_fil.append(op)
    return render(request, 'post/view_project.html', {"project": project, "opinions": op_fil})


def view_thesis(request, pk):
    thesis = Thesis.objects.get(pk=pk)
    if request.method == "POST":
        opinion = request.POST.get('opinion')
        Opinion.objects.create(user=request.user, opinion=opinion, post=thesis)
    opinions = Opinion.objects.all()
    op_fil = []
    for op in opinions:
        if op.post == thesis:
            op_fil.append(op)
    return render(request, 'post/view_thesis.html', {"thesis": thesis, "opinions": op_fil})


def view_event(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == "POST":
        opinion = request.POST.get('opinion')
        Opinion.objects.create(user=request.user, opinion=opinion, post=event)
    opinions = Opinion.objects.all()
    op_fil = []
    for op in opinions:
        if op.post == event:
            op_fil.append(op)
    return render(request, 'post/view_event.html', {"event": event, "opinions": op_fil})


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
