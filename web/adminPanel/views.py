from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm, AboutUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Menu

# Create your views here.
@login_required
def home(request):
    context = {
        'current_path': request.path,
        'home_url': reverse('home')}
    return render(request, "adminPanel/home.html", {'context': context, 'active':'home', 'title': 'Главная страница'})

@login_required
def about(request):
    context = {
        'title': 'О себе',
        'menu': request_menu(request), 
        'active':'about' 
    }
    return render(request, "adminPanel/about.html", context=context)

@login_required
def profile(request):
    context = {
        'current_path': request.path,
        'home_url': reverse('profile')}
    return render(request, "adminPanel/profile.html", {'context': context, 'title': 'Профиль'})

class MyAboutView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        about_form = AboutUpdateForm(instance=request.user.about)
        context = {
            'title': 'О себе',
            'user_form': user_form,
            'profile_form':about_form,
            'active':'about',
            'menu': request_menu(request)
            }

        return render(request, 'adminPanel/about.html', context) 
    
    def post(self,request):
        user_form = UserUpdateForm(
            request.POST, 
            instance=request.user
        )
        about_form = AboutUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.about
        )

        if user_form.is_valid() and about_form.is_valid():
            user_form.save()
            about_form.save()
            
            messages.success(request,'Your profile has been updated successfully')
            
            return redirect('about')
        else:
            context = {
                'title': 'О себе',
                'user_form': user_form,
                'profile_form': about_form,
                'active':'about',
                'menu': request_menu(request)
            }
            messages.error(request,'Error updating you profile')
            
            return render(request, 'adminPanel/about.html', context)

def request_menu(request):
    user_id = request.user.id  # Получаем id текущего пользователя
    menu = Menu.objects.filter(user_id=user_id).first()  # Используем user_id для фильтрации
    # Если вы хотите получить доступ к определенному полю каждого объекта в QuerySet,
    # вам нужно будет перебрать QuerySet, например:

    # print(f"menu - {menu.about}")
    return menu