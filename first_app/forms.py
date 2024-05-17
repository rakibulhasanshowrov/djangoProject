from django import forms
from .models import Musician
class user_form(forms.Form):
    user_name = forms.CharField(label="User Name:",widget=forms.TextInput(attrs={"placeholder":"Enter Name"}))
    #password = forms.CharField(label='密码',widget=forms.PasswordInput)
    user_dob=forms.DateField(label="Date Of Birth",widget=forms.TextInput(
        attrs={"type":"date"}))
    user_email=forms.EmailField()
    
    

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

        
