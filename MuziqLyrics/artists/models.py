from django.db import models

from MuziqLyrics.accounts.models import MuziqUser


# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)

    bio = models.TextField()

    birth_date = models.DateField(null=True, blank=True)

    image = models.ImageField(upload_to='images/', null=True, blank=True)

    user = models.OneToOneField(
        MuziqUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username
