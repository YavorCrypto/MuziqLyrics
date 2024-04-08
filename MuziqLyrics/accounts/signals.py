from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from MuziqLyrics.accounts.models import Listener
from MuziqLyrics.artists.models import Artist

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):

    if not created:
        return

    if instance.account_type == 'Listener':
        Listener.objects.create(user=instance)
    elif instance.account_type == 'Artist':
        Artist.objects.create(user=instance)