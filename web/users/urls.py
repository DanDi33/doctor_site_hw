from django.urls import path
from .views import MyLoginView, RegisterView
from .forms import MyPasswordResetForm, MySetPasswordForm
from django.contrib.auth.views import (LogoutView, 
                                        PasswordResetView, 
                                        PasswordResetDoneView, 
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView
                                    )

urlpatterns = [
    # path("",home , name="home"),
    # path("start/", index, name="index"),
    path("login/", MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password-reset/', PasswordResetView.as_view(template_name="users/password_reset.html",
                                   from_email = "News Site App <kerchek1@yandex.ru>",
                                   form_class = MyPasswordResetForm), name="password_reset"),
    path('password-reset/done/',
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done"
        ),
    path('password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html", 
                                         form_class = MySetPasswordForm),
        name="password_reset_confirm"
        ), 

    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name="password_reset_complete"
         )
  
]