from django.shortcuts import render
from adminPanel.models import Menu, Case
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    user = User.objects.first()
    cases = Case.objects.filter(user_id=user.id)
    context = {
        'title': 'Главная страница',
        'current_path': request.path,
        'active':'home',
        'menu': request_menu(request,user.id),
        'cases': cases,
        'user':user,
        'home_url': reverse('home')
        }
    return render(request, "main/main.html", context=context)

def request_menu(request, user_id):
    # user_id = request.user.id  # Получаем id текущего пользователя
    menu = Menu.objects.filter(user_id=user_id).first()  # Используем user_id для фильтрации
    # Если вы хотите получить доступ к определенному полю каждого объекта в QuerySet,
    # вам нужно будет перебрать QuerySet, например:

    # print(f"menu - {menu.about}")
    return menu