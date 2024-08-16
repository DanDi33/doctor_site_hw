from django.shortcuts import render
from adminPanel.models import Menu, Case, Message, Service, Ed_and_work, Feedback, Contact
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import re


# Create your views here.

class HomeView(CreateView):
    model = Message
    fields = ['name','phone','comment','completed']
    template_name = "main/main.html"

    def form_valid(self, form):
        username = self.kwargs.get('username')

        if not username:
            form.instance.user = User.objects.first()
        else:
            form.instance.user = User.objects.filter(username=username).first()

        form.instance.save()

        phone_number = form.cleaned_data["phone"]
        cleaned_phone = clean_phone_number(phone_number)

        send_mail(
            f'Сообщение от {form.cleaned_data["name"]}',
            f'Вам пришло сообщение от пользователя - "{form.cleaned_data["name"]}", '
            f'телефонный номер - {form.cleaned_data["phone"]}',
            f'Сайт {form.instance.user.get_full_name()}<kerchek1@yandex.ru>',
            [form.instance.user.email],
            fail_silently=False,
            html_message=f'Вам пришло сообщение от пользователя - "{form.cleaned_data["name"]}", '
                         f'телефонный номер - <a href="tel:{cleaned_phone}">'
                         f'{phone_number}</a>',
        )
        messages.success(self.request, "Запись успешно создана.")

        if not username:
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return HttpResponseRedirect(reverse_lazy('site', kwargs={'username': username}))
    
    def get_context_data(self, **kwargs):
        username = self.kwargs.get('username')

        if not username:
            user = User.objects.first()
        else:
            user = User.objects.filter(username=username).first()
            
        context = super(HomeView, self).get_context_data(**kwargs)
        
        cases = Case.objects.filter(user_id=user.id)
        services = Service.objects.filter(user_id=user.id)
        ed_and_works = Ed_and_work.objects.filter(user_id=user.id).order_by('-year')
        feedbacks = Feedback.objects.filter(user_id=user.id)
        contacts = Contact.objects.filter(user_id=user.id)
        context.update({
            'title': 'Главная страница',
            'current_path': self.request.path,
            'active':'home',
            'menu': request_menu(self.request,user.id),
            'cases': cases,
            'services':services,
            'ed_and_works': ed_and_works,
            'feedbacks':feedbacks,
            'contacts':contacts,
            'cur_user':user,
            'home_url': reverse('home')
            })
        return context

def request_menu(request, user_id):
    menu = Menu.objects.filter(user_id=user_id).first()  # Используем user_id для фильтрации
    return menu

def clean_phone_number(phone_number):
    # Удаляем все знаки, кроме цифр и плюса в начале строки
    cleaned_number = re.sub(r'(?<!^)\+|[^\d+]', '', phone_number)
    return cleaned_number