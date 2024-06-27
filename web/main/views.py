from django.shortcuts import render
from adminPanel.models import Menu, Case, Message
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy


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
        messages.success(self.request, "Запись успешно создана.")
        return super(HomeView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user = User.objects.first()
        cases = Case.objects.filter(user_id=user.id)
        context.update({
            'title': 'Главная страница',
            'current_path': self.request.path,
            'active':'home',
            'menu': request_menu(self.request,user.id),
            'cases': cases,
            'user':user,
            'home_url': reverse('home')
            })
        return context

def request_menu(request, user_id):
    # user_id = request.user.id  # Получаем id текущего пользователя
    menu = Menu.objects.filter(user_id=user_id).first()  # Используем user_id для фильтрации
    # Если вы хотите получить доступ к определенному полю каждого объекта в QuerySet,
    # вам нужно будет перебрать QuerySet, например:

    # print(f"menu - {menu.about}")
    return menu