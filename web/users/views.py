from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import RegisterForm, LoginForm, CustomPasswordResetForm
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str
from django.core.mail import EmailMultiAlternatives


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "users/login.html"
    form_class = LoginForm

    def get_success_url(self):
        user = self.request.user
        url = reverse_lazy('site', args=[user.username])
        return url
    
    def form_invalid(self, form):
        messages.error(self.request, 'Неверное имя пользователя или пароль.')
        return self.render_to_response(self.get_context_data(form=form))


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    

class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        users = User.objects.filter(email=email)
        site = get_current_site(self.request)
        current_site = force_str(site.domain)

        if users.exists():
            for user in users:
                context = {
                    'email': user.email,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                    'site_name': site.name,
                    'user': user,
                    'domain': current_site,
                    'protocol': 'https' if self.request.is_secure() else 'http',
                }

                subject = f"Сброс пароля, пользователя - {user.username}"
                body = render_to_string(self.email_template_name, context)
                from_email = f"Сайт {user.get_full_name() or user.username} <kerchek1@yandex.ru>"

                email_message = EmailMultiAlternatives(
                    subject=subject,
                    body=body,
                    from_email=from_email,
                    to=[user.email],
                )
                email_message.send()

        return super().form_valid(form)