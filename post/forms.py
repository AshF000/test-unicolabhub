from django import forms
from .models import Event, Project, Thesis

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer','created_at']
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['organizer','created_at']
        fields = '__all__'

class ThesisForm(forms.ModelForm):
    class Meta:
        model = Thesis
        exclude = ['organizer','created_at']
        fields = '__all__'