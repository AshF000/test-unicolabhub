from django.contrib import admin
from .models import Collaborator,Resource,JoinRequest,Notification

admin.site.register(Collaborator)
admin.site.register(Resource)
admin.site.register(JoinRequest)
admin.site.register(Notification)