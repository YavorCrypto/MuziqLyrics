from django.shortcuts import render

from MuziqLyrics.songs.models import Song


# Create your views here.


def index(request):
    context = {
        'songs': Song.objects.all()
    }
    return render(request, 'web/home_page.html', context)

def contactus(request):
    return render(request, 'web/contact_us.html')