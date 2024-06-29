from django import forms
from django.contrib.auth.models import User
from .models import About, Menu, Paralax

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name"]

class AboutUpdateForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ["profession", "slogan", "main_foto"] 

class UpdateMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['messages','about','services','cases', 'ed_and_work','feedbacks','contacts']

class UpdateParalaxForm(forms.ModelForm):
    class Meta:
        model = Paralax
        fields = ['img1','img2']