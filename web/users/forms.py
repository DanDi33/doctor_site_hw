from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Button, ButtonHolder, HTML
from crispy_forms.bootstrap import Modal

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-registerForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.fields['username'].label = "Имя пользователя"
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Подтверждение пароля"

        self.helper.layout = Layout(
            Field('username'),
            Field('email'),
            Field('password1'),
            Field('password2'),
            ButtonHolder(
                Submit('submit', 'Зарегистрировать'),
                css_class='d-grid gap-2 d-md-flex justify-content-md-end',
            ),
            HTML('<hr><p class="text-center">Уже есть аккаунт? <a href="{% url "login" %}" style="text-decoration: none"> - Авторизуйся!</a></p>'),
        )
        

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-loginForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.fields['username'].label = "Имя пользователя"
        self.fields['password'].label = "Пароль"

        self.helper.layout = Layout(
            Field('username'),
            Field('password'),
            ButtonHolder(
                
                HTML('<a class="btn btn-secondary" href={% url "register" %}>Регистрация</a>'),
                Submit('submit', 'Войти'),
                css_class='d-grid gap-2 d-md-flex justify-content-md-end',
            ),
            HTML('<hr><p class="text-center">Забыли пароль? <a href="{% url "password_reset" %}" style="text-decoration: none"> - Сбросить пароль</a></p>'),
            # Modal(
            #     # email.help_text was set during the initalization of the django form field
            #     Field('email', placeholder="Email", wrapper_class="mb-0"),
            #     Button(
            #         "submit",
            #         "Send Reset Email",
            #         id="email_reset",
            #         css_class="btn-primary mt-3",
            #         onClick="{% url 'home' %}", # used to submit the form
            #     ),
            #     css_id="my_modal_id",
            #     title="This is my modal",
            #     title_class="w-100 text-center",
            # ),
        )


class MyPasswordResetForm(PasswordResetForm):
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()

            self.helper.form_id = 'id-PasswordResetForm'
            self.helper.form_class = 'blueForms'
            self.helper.form_method = 'post'
            self.helper.form_action = 'submit_survey'
            self.helper.layout = Layout(
            Field('email'),
                ButtonHolder(                    
                    HTML('<a class="btn btn-secondary" href={% url "login" %}>Отмена</a>'),
                    Submit('submit', 'Отправить'),
                    css_class='d-grid gap-2 d-md-flex justify-content-md-end',
                ),
             )
            
class MySetPasswordForm(SetPasswordForm):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages = {
            'password_mismatch': "Пароли не совпадают. Пожалуйста, убедитесь, что пароли идентичны."
        }

        self.helper = FormHelper()

        self.helper.form_id = 'id-SetPasswordForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.fields['new_password1'].label = "Пароль"
        self.fields['new_password2'].label = "Подтверждение пароля"

        self.helper.layout = Layout(
        Field('new_password1'),
        Field('new_password2'),
        ButtonHolder(              
                HTML('<a class="btn btn-secondary" href={% url "login" %}>Отмена</a>'),  
                Submit('submit', 'Отправить'),
                css_class='d-grid gap-2 d-md-flex justify-content-md-end',
            ),
        )
          
        