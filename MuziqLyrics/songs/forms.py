from django import forms

from MuziqLyrics.songs.models import Song


class ReadonlyFieldsFormMixin:
    readonly_fields = ()
    def _apply_readonly_on_fields(self):
        for field_name in self.readonly_field_names:
            self.fields[field_name].widget.attrs['readonly'] = 'readonly'
            self.fields[field_name].widget.attrs['disabled'] = 'disabled'

    @property
    def readonly_field_names(self):
        if self.readonly_fields == "__all__":
            return self.fields.keys()
        return self.readonly_fields


class SongBaseForm(forms.ModelForm):
    class Meta:
        model = Song

        fields = ('title', 'artists','genre', 'release_date')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Song Title'}),
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            #'': forms.URLInput(attrs={'placeholder': 'Link to image'})
        }

        labels = {'song': 'Song Title'}


class SongDeleteForm(ReadonlyFieldsFormMixin, SongBaseForm):
    readonly_fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance




