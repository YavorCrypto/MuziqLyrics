from django.shortcuts import render

# Create your views here.


def song_details(request):
    return render(request,'songs/song-details.html')

