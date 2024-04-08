from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from MuziqLyrics.songs.models import Song


@receiver(post_save, sender=Song)
def set_song_artist(sender, instance, created, **kwargs):
    if created:
        user_model = get_user_model()
        user = user_model.objects.get(username=instance.user.username)
        instance.artists.add(user.artist)