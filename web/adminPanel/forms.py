from django import forms
from django.contrib.auth.models import User
from .models import About, Menu, Paralax
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

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

class UserUpdateEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email"]
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот адрес электронной почты уже используется.")
        return email
    
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-control rounded-0 mb-3'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'form-control rounded-0 mb-3'}))
    new_password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-control rounded-0 mb-3'}))
    
    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                "Ваш старый пароль был введен неправильно. Пожалуйста, введите его еще раз."
            )
        return old_password


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label=_("Имя пользователя"), 
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-0 mb-3', 'autocomplete': 'username'}),
    )
    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class': 'form-control rounded-0 mb-3'}),
    )
    password2 = forms.CharField(
        label=_("Подтверждение пароля"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control rounded-0 mb-3'}),
        strip=False,
    )
    email = forms.EmailField(label=_("email"), max_length=254,widget=forms.EmailInput(attrs={'class': 'form-control rounded-0 mb-3'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот адрес электронной почты уже используется.")
        return email