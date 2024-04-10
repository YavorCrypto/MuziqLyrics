from django.urls import path

from MuziqLyrics.web.views import index, contactus

urlpatterns = (
    path('', index, name='index'),
    path('contactus/',contactus, name='contactus')
)