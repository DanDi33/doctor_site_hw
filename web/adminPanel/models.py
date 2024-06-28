from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Menu (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    messages = models.CharField('Сообщения', max_length=100, default="Сообщения")
    about = models.CharField('О себе', max_length=100, default="О себе")
    services = models.CharField('Услуги', max_length=100, default="Услуги")
    cases = models.CharField('Кейсы', max_length=100, default="Кейсы")
    ed_and_work = models.CharField('Образование и работа', max_length=100, default="Образование и работа")
    feedbacks = models.CharField('Отзывы', max_length=100, default="Отзывы")
    contacts = models.CharField('Контакты', max_length=100, default="Контакты")
 
    def __str__(self):
        return f"It's {self.user.username}'s menu"
    
class Message(models.Model):
    name = models.CharField('Имя', max_length=255, null=False, blank=False)
    phone = models.CharField('Номер телефона', max_length=255, null=False, blank=False)
    comment = models.TextField('Комментарий', null=True, blank=True)
    completed = models.BooleanField('Прочитано', default=False)
    created_at = models.DateTimeField('Получено', auto_now_add=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['completed']

class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profession = models.CharField(max_length=200)
    slogan = models.TextField(null=True, blank=True)
    main_foto = models.ImageField(
        default="avatar.jpg",
        upload_to="About_main_foto"
    )

    def __str__(self):
        return f"It's about {self.user.username}"
    

class Service(models.Model):
    title = models.CharField('Название', max_length=200)
    desc = models.TextField('Описание', null=False, blank=False)
    price = models.CharField('Цена', max_length=200, null=True, blank=True)
    img = models.ImageField('Изображение', upload_to="Service_img", null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Case(models.Model):
    post = models.TextField(null=False, blank=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

def current_year():
    return timezone.now().year

class Ed_and_work(models.Model):
    year = models.IntegerField("Год", default=current_year)
    desc = models.TextField(null=False, blank=False)
    diplom_img = models.ImageField(upload_to="Ed_and_work_img", null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Feedback(models.Model):
    name = models.CharField('Имя', max_length=200, null=False, blank=False)
    text = models.TextField('Отзыв', null=False, blank=False)
    original_img = models.ImageField(upload_to="Feedback_img", null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Paralax(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    img1 = models.ImageField('Паралакс 1', upload_to="paralax_img", null=False, blank=False, default='fon.jpg')
    img2 = models.ImageField('Паралакс 2', upload_to="paralax_img", null=False, blank=False, default='fon.jpg')

    def __str__(self):
        return f"It's {self.user.username}'s paralax"