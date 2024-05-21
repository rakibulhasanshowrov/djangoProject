from django import forms
from first_app import models

class add_musician_form(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = '__all__'


class add_album_form(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = '__all__'
        
