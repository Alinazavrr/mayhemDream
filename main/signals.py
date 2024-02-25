from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_custom_user(sender, instance, created, **kwargs):
    if created:
        # Вытащим instance из kwargs
        # instance = kwargs.get('instance', None)  # Эта строка не нужна, так как instance уже передается как первый параметр
        UserProfile.objects.create(user=instance)