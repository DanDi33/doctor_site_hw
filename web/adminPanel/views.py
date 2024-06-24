from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm, AboutUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Menu, Ed_and_work
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

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

class MyEdAndWorkView(LoginRequiredMixin,ListView):
    model = Ed_and_work
    template_name = "adminPanel/ed-and-work.html"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Образование и работа'
        context['posts'] = context['posts'].filter(user=self.request.user).order_by('year')
        context['active'] = 'ed_and_work'
        context['menu'] = request_menu(self.request)
        return context

class CreatePostEdAndWorkView(LoginRequiredMixin,CreateView):
    model = Ed_and_work
    fields = ['year','desc','diplom_img']
    template_name = "adminPanel/ed-and-work-form.html"
    success_url = reverse_lazy('ed_and_work')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Запись успешно создана.")
        return super(CreatePostEdAndWorkView,self).form_valid(form)

def request_menu(request):
    user_id = request.user.id  # Получаем id текущего пользователя
    menu = Menu.objects.filter(user_id=user_id).first()  # Используем user_id для фильтрации
    # Если вы хотите получить доступ к определенному полю каждого объекта в QuerySet,
    # вам нужно будет перебрать QuerySet, например:

    # print(f"menu - {menu.about}")
    return menu