from typing import Any
from django import forms

class second_form(forms.Form):
    user_name=forms.CharField()
    boolean_field=forms.BooleanField()


def even_or_not(value):
    if value%2==1:
        print(value)
        raise forms.ValidationError("Not an even Number")
        
class form_validation_test(forms.Form):
    print(' class initiated')
    numberField=forms.IntegerField(label="Number Validation",validators=[even_or_not])
    
class emailVerification(forms.Form):
    email=forms.EmailField(label="Enter Email")
    vemail=forms.EmailField(label="Enter Email Again")
    
    def clean(self):
        cleaned_data=super().clean()
        email=cleaned_data['email']
        vemail=cleaned_data['vemail']
        if email !=vemail:
            raise forms.ValidationError("Emails do not match")