from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)

    bio = models.TextField()

    birth_date = models.DateField(null=True, blank=True)

    image = models.ImageField(upload_to='artist_images/', null=True, blank=True)

    def __str__(self):
        return self.name
