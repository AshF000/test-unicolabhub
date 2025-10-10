from django.db import models

class Event(models.Model):
    organizer = models.ForeignKey("User", on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    cover = models.ImageField(upload_to="photos/", null=True, blank=True)
    schedule = models.ImageField(upload_to="photos/", null=True, blank=True)


