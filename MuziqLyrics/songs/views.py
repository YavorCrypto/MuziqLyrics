from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from MuziqLyrics.songs.models import Song


# Create your views here.


def song_details(request):
    return render(request,'songs/song-details.html')


class SongDetailsView(views.DetailView):
    queryset = Song.objects.all()
    template_name = 'songs/song-details.html'


class SongAddView(views.CreateView):
    queryset = Song.objects.all()
    fields = ('title','artists','lyrics','release_date','genre')
    template_name = 'songs/song-add.html'
    success_url = reverse_lazy('index')


