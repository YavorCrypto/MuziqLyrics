from django.urls import path

from MuziqLyrics.songs.views import song_details, SongDetailsView, SongAddView

urlpatterns = (
    path('add/',SongAddView.as_view(),name='song_add'),
    path('<int:pk>/details/',SongDetailsView.as_view(),name='song_details'),
    #path('<int:pk>/delete/') ...
)