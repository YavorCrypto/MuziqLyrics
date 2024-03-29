from django.db import models

from MuziqLyrics.artists.models import Artist


# Create your models here.


class Album(models.Model):

    title = models.CharField(max_length=100)

    release_date = models.DateField(auto_now_add=True)

    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return self.title