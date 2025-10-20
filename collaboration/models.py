from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


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
