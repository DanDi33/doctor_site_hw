from django.shortcuts import render
from adminPanel.models import Menu, Case, Message, Service, Ed_and_work, Feedback
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail
import re


# Create your views here.

# def home(request):
#     user = User.objects.first()
#     cases = Case.objects.filter(user_id=user.id)

#     context = {
#         'title': 'Главная страница',
#         'current_path': request.path,
#         'active':'home',
#         'menu': request_menu(request,user.id),
#         'cases': cases,
#         'user':user,
#         'home_url': reverse('home')
#         }
#     return render(request, "main/main.html", context=context)

class HomeView(CreateView):
    model = Message
    fields = ['name','phone','comment','completed']
    template_name = "main/main.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = User.objects.first()
        phone_number = form.cleaned_data["phone"]
        cleaned_phone = clean_phone_number(phone_number)
        print(f"cleaned phone - {cleaned_phone}")
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
        return super(HomeView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = User.objects.first()
        cases = Case.objects.filter(user_id=user.id)
        services = Service.objects.filter(user_id=user.id)
        ed_and_works = Ed_and_work.objects.filter(user_id=user.id)
        feedbacks = Feedback.objects.filter(user_id=user.id)
        context.update({
            'title': 'Главная страница',
            'current_path': self.request.path,
            'active':'home',
            'menu': request_menu(self.request,user.id),
            'cases': cases,
            'services':services,
            'ed_and_works': ed_and_works,
            'feedbacks':feedbacks,
            'cur_user':user,
            'home_url': reverse('home')
            })
        return context

def request_menu(request, user_id):
    # user_id = request.user.id  # Получаем id текущего пользователя
    menu = Menu.objects.filter(user_id=user_id).first()  # Используем user_id для фильтрации

    # print(f"menu - {menu.about}")
    return menu

def clean_phone_number(phone_number):
    # Удаляем все знаки, кроме цифр и плюса в начале строки
    cleaned_number = re.sub(r'(?<!^)\+|[^\d+]', '', phone_number)
    return cleaned_number