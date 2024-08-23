from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (UserUpdateForm, 
                    AboutUpdateForm, 
                    UpdateMenuForm, 
                    UpdateParalaxForm, 
                    UserUpdateEmailForm,
                    UserPasswordChangeForm,
                    RegisterForm)
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Menu, Message, Service, Case, Ed_and_work, Feedback, Contact, LogMessage
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.


class MessagesView(LoginRequiredMixin,ListView):
    model = Message
    template_name = "adminPanel/messages.html"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user_id=self.request.user.id)
        context['title'] = 'Сообщения'
        context['active'] = 'messages'
        context['menu'] = request_menu(self.request)
        context['unread_count'] = Message.objects.filter(user_id=self.request.user.id, completed=False).count()
        return context
    
    def get_queryset(self):
        return Message.objects.all().order_by('-created_at')


class UpdateMessageView(LoginRequiredMixin,UpdateView):
    model = Message
    fields = ['comment','completed']
    template_name = "adminPanel/message-form.html"
    success_url = reverse_lazy('messages')


    def form_valid(self, form):

        message = form.save(commit=False)
        formatted_date = timezone.localtime(message.created_at).strftime('%d-%m-%Y %H:%M:%S')
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'Сообщение от {message.name}, созданное {formatted_date}  - изменено.'
        )

        form.instance.user = self.request.user
        messages.success(self.request, "Запись успешно изменена.")
        return super(UpdateMessageView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(UpdateMessageView, self).get_context_data(**kwargs)
        context['active'] = 'messages'
        context['menu'] = request_menu(self.request)
        return context


class DeleteMessageView(LoginRequiredMixin,DeleteView):
    model = Message    
    success_url = reverse_lazy('messages')

    def form_valid(self, form):

        message = self.get_object()
        formatted_date = timezone.localtime(message.created_at).strftime('%d-%m-%Y %H:%M:%S')
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'Сообщение от {message.name}, созданное {formatted_date}  - удалено.'
        )

        messages.success(self.request, "Сообщение успешно удалено.")
        return super(DeleteMessageView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(DeleteMessageView, self).get_context_data(**kwargs)
        context['active'] = 'messages'
        context['menu'] = request_menu(self.request)
        return context
    

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

        user_form_valid = user_form.is_valid()
        about_form_valid = about_form.is_valid()

        if user_form_valid:
            user_form.save()
        if about_form_valid:
            about_form.save()

        if user_form_valid or about_form_valid:
           
            LogMessage.objects.create(
                username=self.request.user.username,
                text=f'Блок "О себе" - изменен.'
            )
            messages.success(request,'Ваш блок "О себе" успешно изменен.')
            return redirect('about')
        
        context = {
            'title': 'О себе',
            'user_form': user_form,
            'profile_form': about_form,
            'active':'about',
            'menu': request_menu(request)
        }
           
        messages.error(request, 'Ошибка изменения блока "О себе". Проверьте формы и попробуйте снова.')
        return render(request, 'adminPanel/about.html', context)


class ServiceView(LoginRequiredMixin,ListView):
    model = Service
    template_name = "adminPanel/services.html"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user_id=self.request.user.id)
        context['title'] = 'Услуги'
        context['active'] = 'services'
        context['menu'] = request_menu(self.request)
        return context


class CreateServiceView(LoginRequiredMixin,CreateView):
    model = Service
    fields = ['title','desc','price','img']
    template_name = "adminPanel/service-form.html"
    success_url = reverse_lazy('services')


    def form_valid(self, form):

        service = form.save(commit=False)
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Услуги" запись "{service.title}" - создана.'
        )

        form.instance.user = self.request.user
        messages.success(self.request, "Запись успешно создана.")
        return super(CreateServiceView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CreateServiceView, self).get_context_data(**kwargs)
        context['active'] = 'services'
        context['menu'] = request_menu(self.request)
        return context


class UpdateServiceView(LoginRequiredMixin,UpdateView):
    model = Service
    fields = ['title','desc','price','img']
    template_name = "adminPanel/service-form.html"
    success_url = reverse_lazy('services')


    def form_valid(self, form):

        service = form.save(commit=False)
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Услуги" запись "{service.title}" - изменена.'
        )

        form.instance.user = self.request.user
        messages.success(self.request, "Запись успешно изменена.")
        return super(UpdateServiceView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(UpdateServiceView, self).get_context_data(**kwargs)
        context['active'] = 'services'
        context['menu'] = request_menu(self.request)
        return context


class DeleteServiceView(LoginRequiredMixin,DeleteView):
    model = Service    
    success_url = reverse_lazy('services')

    def form_valid(self, form):

        service = self.get_object()
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Услуги" запись "{service.title}" - удалена.'
        )

        messages.success(self.request, "Запись успешно удалена.")
        return super(DeleteServiceView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(DeleteServiceView, self).get_context_data(**kwargs)
        context['active'] = 'services'
        context['menu'] = request_menu(self.request)
        return context


class MyEdAndWorkView(LoginRequiredMixin,ListView):
    model = Ed_and_work
    template_name = "adminPanel/ed-and-work.html"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user_id=self.request.user.id)
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

        ed_and_work = form.save(commit=False)
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Образование и работа" запись "{ed_and_work.desc[:40]}..." - создана.'
        )

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

        ed_and_work = form.save(commit=False)
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Образование и работа" запись "{ed_and_work.desc[:40]}..." - изменена.'
        )

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

        ed_and_work = self.get_object()
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Образование и работа" запись "{ed_and_work.desc[:40]}..." - удалена.'
        )

        messages.success(self.request, "Запись успешно удалена.")
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
        context['posts'] = context['posts'].filter(user_id=self.request.user.id)
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

        case = form.save(commit=False)
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Кейсы" запись "{case.post[:40]}..." - создана.'
        )

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

        case = form.save(commit=False)
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Кейсы" запись "{case.post[:40]}..." - изменена.'
        )

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

        case = self.get_object()
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Кейсы" запись "{case.post[:40]}..." - удалена.'
        )

        messages.success(self.request, "Запись успешно удалена.")
        return super(DeleteCaseView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(DeleteCaseView, self).get_context_data(**kwargs)
        context['active'] = 'cases'
        context['menu'] = request_menu(self.request)
        return context


class  FeedbackView(LoginRequiredMixin,ListView):
    model = Feedback
    template_name = "adminPanel/feedbacks.html"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user_id=self.request.user.id)
        context['title'] = 'Отзывы'
        context['active'] = 'feedbacks'
        context['menu'] = request_menu(self.request)
        return context
    

class CreateFeedbackView(LoginRequiredMixin,CreateView):
    model = Feedback
    fields = ['name','text','original_img']
    template_name = "adminPanel/feedback-form.html"
    success_url = reverse_lazy('feedbacks')


    def form_valid(self, form):

        feedback = form.save(commit=False)
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Отзывы" отзыв от "{feedback.name}" - создан.'
        )


        form.instance.user = self.request.user
        messages.success(self.request, "Отзыв успешно создана.")
        return super(CreateFeedbackView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CreateFeedbackView, self).get_context_data(**kwargs)
        context['active'] = 'feedbacks'
        context['menu'] = request_menu(self.request)
        return context
    

class UpdateFeedbackView(LoginRequiredMixin,UpdateView):
    model = Feedback
    fields = ['name','text','original_img']
    template_name = "adminPanel/feedback-form.html"
    success_url = reverse_lazy('feedbacks')


    def form_valid(self, form):

        feedback = form.save(commit=False)
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Отзывы" отзыв от "{feedback.name}" - изменен.'
        )

        form.instance.user = self.request.user
        messages.success(self.request, "Отзыв успешно изменен.")
        return super(UpdateFeedbackView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(UpdateFeedbackView, self).get_context_data(**kwargs)
        context['active'] = 'feedbacks'
        context['menu'] = request_menu(self.request)
        return context
    

class DeleteFeedbackView(LoginRequiredMixin,DeleteView):
    model = Feedback    
    success_url = reverse_lazy('feedbacks')

    def form_valid(self, form):

        feedback = self.get_object()
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Отзывы" отзыв от "{feedback.name}" - удален.'
        )

        messages.success(self.request, "Отзыв успешно удален.")
        return super(DeleteFeedbackView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(DeleteFeedbackView, self).get_context_data(**kwargs)
        context['active'] = 'feedbacks'
        context['menu'] = request_menu(self.request)
        return context   


class ContactView(LoginRequiredMixin,ListView):
    model = Contact
    template_name = "adminPanel/contact.html"
    context_object_name = "posts"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(user_id=self.request.user.id)
        context['title'] = 'Контакты'
        context['active'] = 'contacts'
        context['menu'] = request_menu(self.request)
        return context
    

class CreateContactView(LoginRequiredMixin,CreateView):
    model = Contact
    fields = ['post']
    template_name = "adminPanel/contact-form.html"
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):

        contact = form.save(commit=False)
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Контакты" запись "{contact.post[:40]}..." - создана.'
        )

        form.instance.user = self.request.user
        messages.success(self.request, "Запись успешно создана.")
        return super(CreateContactView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['active'] = 'contacts'
        context['menu'] = request_menu(self.request)
        return context


class UpdateContactView(LoginRequiredMixin,UpdateView):
    model = Contact
    fields = ['post']
    template_name = "adminPanel/contact-form.html"
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):

        contact = form.save(commit=False)
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Контакты" запись "{contact.post[:40]}..." - изменена.'
        )

        form.instance.user = self.request.user
        messages.success(self.request, "Запись успешно изменена.")
        return super(UpdateContactView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['active'] = 'contacts'
        context['menu'] = request_menu(self.request)
        return context
    

class DeleteContactView(LoginRequiredMixin,DeleteView):
    model = Contact    
    success_url = reverse_lazy('contacts')

    def form_valid(self, form):

        contact = self.get_object()
        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'В блоке "Контакты" запись "{contact.post[:40]}..." - удалена.'
        )

        messages.success(self.request, "Запись успешно удалена.")
        return super(DeleteContactView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(DeleteContactView, self).get_context_data(**kwargs)
        context['active'] = 'contacts'
        context['menu'] = request_menu(self.request)
        return context


class UpdateMenuView(LoginRequiredMixin, View):
    # login_url = '/login/'
    
    def get(self, request):

        menu_form = UpdateMenuForm(instance=request.user.menu)
        str = ['messages','about', 'services', 'cases']
        context = {      
            'menu_form':menu_form,
            'active':'settings-menu',
            'menu':request_menu(self.request),
            'str':str
        }

        return render(request, 'adminPanel/settings-menu.html', context) 
    
    def post(self,request):

        menu_form = UpdateMenuForm(
            request.POST,
            instance=request.user.menu
        )

        if menu_form.is_valid():

            LogMessage.objects.create(
                username=self.request.user.username,
                text=f'Изменено "Меню".'
            )

            menu_form.save()     
            messages.success(request,'Меню успешно изменено.')       
            return redirect('settings-menu')
        
        else:
            context = {
                'menu_form': menu_form,
                'active':'settings-menu',
                'menu':request_menu(self.request)
            }
            messages.error(request,'Ошибка при изменении меню')
            
            return render(request, 'adminPanel/settings-menu.html', context)


class UpdateParalaxView(LoginRequiredMixin, View):
    # login_url = '/login/'
    
    def get(self, request):
        paralax_form = UpdateParalaxForm(instance=request.user.paralax)
        context = {
            'title': 'Настройки - картинки паралакс',
            'paralax_form': paralax_form,
            'active':'settings-paralax',
            'menu': request_menu(request)
            }

        return render(request, 'adminPanel/settings-paralax.html', context) 
    
    def post(self,request):
        paralax_form = UpdateParalaxForm(
            request.POST,
            request.FILES,
            instance=request.user.paralax
        )

        if paralax_form.is_valid():

            LogMessage.objects.create(
            username=self.request.user.username,
            text=f'Изменены "Паралакс-картинки".'
            )

            paralax_form.save()      
            messages.success(request,'Форма успешна изменена.')
            
            return redirect('settings-paralax')
        else:
            context = {
                'title': 'Настройки - картинки паралакс',
                'paralax_form': paralax_form,
                'active':'settings-paralax',
                'menu': request_menu(request)
            }
            messages.error(request,'Ошибка при изменении формы.')
            
            return render(request, 'adminPanel/settings-paralax.html', context=context)


class UserListView(LoginRequiredMixin,ListView):
    model = User
    template_name = "adminPanel/settings-users.html"
    context_object_name = "posts"

    def get_queryset(self):
        return User.objects.filter(is_superuser=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        context['active'] = 'settings-users'
        context['menu'] = request_menu(self.request)
        return context
    
    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_superuser:
            messages.error(request, 'У Вас нет прав для просмотра списка пользователей.')
            return redirect('profile')

        return super().dispatch(request, *args, **kwargs)


class DeleteUserView(LoginRequiredMixin,DeleteView):
    model = User 
    template_name = "adminPanel/user_confirm_delete.html"
    success_url = reverse_lazy('settings-users')

    def form_valid(self, form):

        deleted_user = self.get_object()

        if deleted_user.is_superuser:
            messages.error(self.request, f"Невозможно удалить суперюзера '{deleted_user.username}'.")
            return redirect('settings-users')

        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'Пользователь "{deleted_user.username}" - успешно удален.'
        )

        messages.success(self.request, f"Пользователь '{deleted_user.username}' - успешно удален.")
        return super(DeleteUserView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(DeleteUserView, self).get_context_data(**kwargs)
        context['active'] = 'settings-users'
        context['menu'] = request_menu(self.request)
        return context
    
    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_superuser:
            messages.error(request, 'У Вас нет прав для удаления пользователей.')
            return redirect('profile')

        return super().dispatch(request, *args, **kwargs)


class  LogsView(LoginRequiredMixin,ListView):
    model = LogMessage
    template_name = "adminPanel/settings-logs.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return LogMessage.objects.all().order_by('-created_at')
        else:
            return LogMessage.objects.filter(username=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Логи'
        context['active'] = 'settings-logs'
        context['menu'] = request_menu(self.request)
        return context


class ProfileView(LoginRequiredMixin, View):
    
    def get(self, request):
        user_form = UserUpdateEmailForm(instance=request.user)

        context = {
            'title': 'Профиль',
            'user_form': user_form,
            'menu': request_menu(request)
            }

        return render(request, 'adminPanel/profile.html', context) 
    
    def post(self,request):
        user_form = UserUpdateEmailForm(
            request.POST, 
            instance=request.user
        )

        if user_form.is_valid():
            user_form.save()

            LogMessage.objects.create(
                username=self.request.user.username,
                text=f'E-mail изменен.'
        )
            
            messages.success(request,'E-mail успешно изменен.')
            
            return redirect('profile')
        else:
            context = {
                'title': 'Профиль',
                'user_form': user_form,
                'menu': request_menu(request)
            }
            print(f"errors - {user_form.errors}")
            messages.error(request,user_form.errors)
            
            return render(request, 'adminPanel/profile.html', context)


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "adminPanel/password_change_form.html"
    extra_context = {'title': "Изменение пароля"}
    
    def form_valid(self, form):

        LogMessage.objects.create(
            username=self.request.user.username,
            text=f'Пароль изменен.'
        )

        return super(UserPasswordChange, self).form_valid(form)


class RegisterView(FormView):
    template_name = 'adminPanel/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = False
    success_url = reverse_lazy('about')

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_superuser:
            messages.error(request, 'У Вас нет прав регистрировать новых пользователей.')
            return redirect('profile')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            LogMessage.objects.create(
                username=self.request.user.username,
                text=f'Зарегистрирован новый пользователь - {user.username}'
                )

        return super(RegisterView, self).form_valid(form)


def request_menu(request):
    user_id = request.user.id  # Получаем id текущего пользователя
    menu = Menu.objects.filter(user_id=user_id).first()  # Используем user_id для фильтрации

    # print(f"menu - {menu.about}")
    return menu