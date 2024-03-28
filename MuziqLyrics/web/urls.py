from django.urls import path

from MuziqLyrics.web.views import index

urlpatterns = (
    path('', index, name='index'),
)