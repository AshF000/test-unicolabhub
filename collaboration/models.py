
from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone


class Collaborator(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=120)
    status = models.CharField(max_length=120)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    post = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.user.username

class Resource(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    type = models.CharField(max_length=120)
    amount = models.PositiveIntegerField()
    university = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    image = models.ImageField(upload_to="photos/", null=True, blank=True, default=None)

    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    allocated_to = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    read_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username + ": " + self.message

class JoinRequest(models.Model):
    organizer = models.ForeignKey(Collaborator, on_delete=models.SET_NULL, null=True)
    recipient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    notification = models.ForeignKey(Notification, on_delete=models.SET_NULL, null=True)
    approve_status = models.CharField(max_length=120, default="not approved")

    def __str__(self):
        return self.organizer.user.username + ": " + self.recipient.username + ": " + self.approve_status
