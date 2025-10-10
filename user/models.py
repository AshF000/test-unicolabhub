from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class CollabUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    collaborator_phone = models.CharField(max_length=20, default='', blank=True)
    collaborator_department = models.CharField(max_length=20, default='', blank=True)
    collaborator_university = models.CharField(max_length=20, default='', blank=True)
    collaborator_date_of_birth = models.DateField(blank=True, null=True)
    collaborator_university_id = models.CharField(max_length=20, default='', blank=True)
    collaborator_type = models.CharField(max_length=20, default='', blank=True)
    collaborator_about = models.CharField(max_length=20, default='', blank=True)

    collaborator_joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return (self.user.username+" "+self.collaborator_university+" "+self.collaborator_university_id)


class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    opinion = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    post = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.opinion[0:20]