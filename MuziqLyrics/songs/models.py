from django.db import models

from MuziqLyrics.albums.models import Album
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

    release_date = models.DateField(auto_now_add=True)

    genre = models.CharField(
        max_length=20,
        choices=GENRE_CHOICES,
    )

    cover_image = models.URLField(default='https://gibus.be/wp-content/uploads/woocommerce-placeholder-1000x1000.png')

    album = models.ForeignKey(Album,blank=True, null=True, on_delete=models.CASCADE)
