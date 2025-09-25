from django import forms
from django.contrib.auth.models import User
from .models import CollabUser

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class CollabUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CollabUser
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'collaborator_date_of_birth': forms.DateInput(
                attrs={'placeholder': 'YYYY-MM-DD'} # Visible hint
            )

        }