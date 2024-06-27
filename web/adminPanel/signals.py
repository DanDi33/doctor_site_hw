from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from adminPanel.models import Menu, About, Paralax

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Menu.objects.create(user=instance)
        About.objects.create(user=instance)
        Paralax.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.menu.save()
    instance.about.save()
    instance.paralax.save()