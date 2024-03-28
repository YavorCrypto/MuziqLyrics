from django.urls import path

from MuziqLyrics.songs.views import song_details

urlpatterns = (
    path('details/',song_details,name='song_details'),
)