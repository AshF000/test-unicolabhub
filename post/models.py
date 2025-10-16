from django.db import models
from collaboration.models import Collaborator
from django.utils import timezone

class Event(models.Model):
    organizer = models.ForeignKey(Collaborator, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    cover_pic = models.ImageField(upload_to="photos/", null=True, blank=True,default=None)
    schedule = models.ImageField(upload_to="photos/", null=True, blank=True,default=None)
    created_at = models.DateTimeField(default=timezone.now)


class Project(models.Model):
    organizer = models.ForeignKey(Collaborator, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    deadline = models.DateField()
    status = models.CharField(max_length=100)
    cover_pic = models.ImageField(upload_to="photos/", null=True, blank=True,default=None)
    criteria = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


class Thesis(models.Model):
    organizer = models.ForeignKey(Collaborator, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    research_topic = models.CharField(max_length=100)
    research_field = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100)
    cover_pic = models.ImageField(upload_to="photos/", null=True, blank=True,default=None)
    created_at = models.DateTimeField(default=timezone.now)
