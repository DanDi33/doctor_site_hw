from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm, AboutUpdateForm, UpdateMenuForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Menu, Case, Ed_and_work
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

# @login_required
# def about(request):
#     context = {
#         'title': 'О себе',
#         'menu': request_menu(request), 
#         'active':'about' 
#     }
#     return render(request, "adminPanel/about.html", context=context)

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
    success_url = reverse_lazy('ed-and-work')


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Запись успешно создана.")
        return super(CreatePostEdAndWorkView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CreatePostEdAndWorkView, self).get_context_data(**kwargs)
        context['active'] = 'ed_and_work'
        context['menu'] = request_menu(self.request)
        return context
    
class UpdatePostEdAndWorkView(LoginRequiredMixin,UpdateView):
    model = Ed_and_work
    fields = ['year','desc','diplom_img']
    template_name = "adminPanel/ed-and-work-form.html"
    success_url = reverse_lazy('ed-and-work')


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Запись успешно изменена.")
        return super(UpdatePostEdAndWorkView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(UpdatePostEdAndWorkView, self).get_context_data(**kwargs)
        context['active'] = 'ed_and_work'
        context['menu'] = request_menu(self.request)
        return context

class DeletePostEdAndWorkView(LoginRequiredMixin,DeleteView):
    model = Ed_and_work    
    success_url = reverse_lazy('ed-and-work')

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно удалена. !")
        return super(DeletePostEdAndWorkView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(DeletePostEdAndWorkView, self).get_context_data(**kwargs)
        context['active'] = 'ed_and_work'
        context['menu'] = request_menu(self.request)
        return context
    
class MyCaseView(LoginRequiredMixin,ListView):
    model = Case
    template_name = "adminPanel/case.html"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Решаемые проблемы'
        context['active'] = 'cases'
        context['menu'] = request_menu(self.request)
        return context

class CreateCaseView(LoginRequiredMixin,CreateView):
    model = Case
    fields = ['post']
    template_name = "adminPanel/case-form.html"
    success_url = reverse_lazy('cases')


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Запись успешно создана.")
        return super(CreateCaseView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CreateCaseView, self).get_context_data(**kwargs)
        context['active'] = 'cases'
        context['menu'] = request_menu(self.request)
        return context
    
class UpdateCaseView(LoginRequiredMixin,UpdateView):
    model = Case
    fields = ['post']
    template_name = "adminPanel/case-form.html"
    success_url = reverse_lazy('cases')


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Запись успешно изменена.")
        return super(UpdateCaseView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(UpdateCaseView, self).get_context_data(**kwargs)
        context['active'] = 'cases'
        context['menu'] = request_menu(self.request)
        return context
    
class DeleteCaseView(LoginRequiredMixin,DeleteView):
    model = Case    
    success_url = reverse_lazy('cases')

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно удалена. !")
        return super(DeleteCaseView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(DeleteCaseView, self).get_context_data(**kwargs)
        context['active'] = 'cases'
        context['menu'] = request_menu(self.request)
        return context

# class UpdateMenuView(LoginRequiredMixin,UpdateView):
#     model = Menu
#     fields = ['about','services','cases', 'ed_and_work','feedbackes']
#     template_name = "adminPanel/menu-settings.html"
#     success_url = reverse_lazy('cases')


#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         messages.success(self.request, "Запись успешно изменена.")
#         return super(UpdateMenuView,self).form_valid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super(UpdateMenuView, self).get_context_data(**kwargs)
#         context['active'] = 'username'
#         context['menu'] = request_menu(self.request)
#         return context

class UpdateMenuView(LoginRequiredMixin, View):
    # login_url = '/login/'
    
    def get(self, request):

        menu_form = UpdateMenuForm(instance=request.user.menu)
        str = ['about', 'services', 'cases']
        context = {      
            'menu_form':menu_form,
            'active':'menu-settings',
            'menu':request_menu(self.request),
            'str':str
        }

        return render(request, 'adminPanel/menu-settings.html', context) 
    
    def post(self,request):

        menu_form = UpdateMenuForm(
            request.POST,
            instance=request.user.menu
        )

        if menu_form.is_valid():
            menu_form.save()
            
            messages.success(request,'Your profile has been updated successfully')
            
            return redirect('menu-settings')
        else:
            context = {
                'menu_form': menu_form,
                # 'active':'username',
                # 'menu':request_menu(self.request)
            }
            messages.error(request,'Error updating you profile')
            
            return render(request, 'adminPanel/menu-settings.html', context)

def request_menu(request):
    user_id = request.user.id  # Получаем id текущего пользователя
    menu = Menu.objects.filter(user_id=user_id).first()  # Используем user_id для фильтрации
    # Если вы хотите получить доступ к определенному полю каждого объекта в QuerySet,
    # вам нужно будет перебрать QuerySet, например:

    # print(f"menu - {menu.about}")
    return menu