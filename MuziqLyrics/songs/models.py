from django.db import models

from MuziqLyrics.artists.models import Artist


# Create your models here.


class Song(models.Model):

    GENRE_CHOICES = [
        ('Classical', 'Classical'),
        ('Jazz', 'Jazz'),
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Hip Hop', 'Hip Hop'),
        ('Country', 'Country'),
        ('Electronic', 'Electronic'),
    ]

    title = models.CharField(max_length=100)

    artists = models.ManyToManyField(Artist)

    lyrics = models.TextField()

    release_date = models.DateField()

    genre = models.CharField(
        max_length=20,
        choices=GENRE_CHOICES,
    )
