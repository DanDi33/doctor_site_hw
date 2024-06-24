from django import forms
from django.contrib.auth.models import User
from .models import About

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name"]

class AboutUpdateForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ["profession", "main_foto"] 