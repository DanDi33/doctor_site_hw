from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
# from PIL import Image

# Create your models here.
class Menu (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    about = models.CharField(max_length=100, default="О себе")
    services = models.CharField(max_length=100, default="Услуги")
    cases = models.CharField(max_length=100, default="Кейсы")
    Ed_and_work = models.CharField(max_length=100, default="Образование и работа")
    feedbackes = models.CharField(max_length=100, default="Отзывы")




# class Phone(models.Model):
#     phone = PhoneNumberField(null=False, blank=False, unique=True)
#     main = models.BooleanField(default=False)

#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def save(self, *args, **kwargs):
#         if self.main:
#             # Установка значения поля 'main' в 'False' для всех других записей пользователя
#             Phone.objects.filter(user=self.user).update(main=False)
#         super(Phone, self).save(*args, **kwargs)


class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profession = models.CharField(max_length=200)
    main_foto = models.ImageField(
        default="avatar.jpg",
        upload_to="About_main_foto"
    )

    def __str__(self):
        return f"{self.user.username} Profile"
    
    # def save(self, *args, **kwargs):
    #     super().save(*args,**kwargs)
        
        # img = Image.open(self.avatar.path)
        # if img.height > 300 or img.width > 300:
        #     output_size = (300,300)
        #     img.thumbnail(output_size)
        #     img.save(self.avatar.path)
