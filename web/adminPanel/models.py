from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Menu (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    about = models.CharField(max_length=100, default="О себе")
    services = models.CharField(max_length=100, default="Услуги")
    cases = models.CharField(max_length=100, default="Кейсы")
    ed_and_work = models.CharField(max_length=100, default="Образование и работа")
    feedbackes = models.CharField(max_length=100, default="Отзывы")


class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profession = models.CharField(max_length=200)
    main_foto = models.ImageField(
        default="avatar.jpg",
        upload_to="About_main_foto"
    )

    def __str__(self):
        return f"{self.user.username} Profile"
    

def current_year():
    return timezone.now().year

class Ed_and_work(models.Model):
    year = models.IntegerField("Год", default=current_year)
    desc = models.TextField(null=False, blank=False)
    diplom_img = models.ImageField(upload_to="Ed_and_work_img")

    user = models.ForeignKey(User, on_delete=models.CASCADE)