from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from MuziqLyrics.songs.models import Song


# Create your views here.


# def song_details(request):
#     return render(request,'songs/song-details.html')


class SongDetailsView(views.DetailView):
    queryset = Song.objects.all()
    template_name = 'songs/song-details.html'


class SongAddView(views.CreateView):
    queryset = Song.objects.all()
    fields = ('title','artists','lyrics','album','genre','cover_image')
    template_name = 'songs/song-add.html'
    success_url = reverse_lazy('index')


# class SongDeleteView(views.DeleteView):
#     queryset = Song.objects.all()
#     form_class = SongDeleteForm
#
#     template_name ='songs/song-delete.html'
#     success_url = reverse_lazy('index')
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['instance'] = self.object
#         return kwargs


class SongEditView(views.UpdateView):
    queryset = Song.objects.all()
    template_name = 'songs/song-edit.html'
    fields = ('title', 'lyrics', 'genre', 'cover_image')
    success_url =reverse_lazy('index')


class SongDeleteView(views.DeleteView):
    queryset = Song.objects.all()
    template_name = 'songs/song-delete.html'

    form_class = modelform_factory(
        Song,
        fields=('title', 'artists','genre','album'),
    )

    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profile'] = Profile.objects.first()
    #     return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['disabled'] = True
        return form


