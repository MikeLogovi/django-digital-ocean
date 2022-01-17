from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model
from .models import Lead

from django.contrib.auth.views import LoginView

class LeadModelForm(forms.ModelForm):
    class Meta:
        model= Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )


class CustomUserFormCreation(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {'username': UsernameField}
