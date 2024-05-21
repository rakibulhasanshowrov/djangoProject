from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician
from first_app import forms


# Create your views here.
def index(request):
    musician_list=Musician.objects.order_by('first_name')
    dict={
        'key1':"I am learning Django. Here passing a value from views Function",
        "musician":musician_list
        
    }
    return render(request,'first_app/index.html',context=dict)


def form(request):
    new_form=forms.user_form()
    dict={
        "key1":"this is from Django Built In Form Library",
        "form":new_form
    }
    
    if request.method=="POST":
        new_form=forms.user_form(request.POST)
        if new_form.is_valid():
            user_name=new_form.cleaned_data['user_name']
            user_dob=new_form.cleaned_data['user_dob']
            user_email=new_form.cleaned_data['user_email']
            dict.update({"user_name":user_name})
            dict.update({'user_dob':user_dob})
            dict.update({'user_email':user_email})
            dict.update({'form_submitted':'yes'})
            
            
    return  render(request,"first_app/form.html",context=dict)

def addMusician(request):
    new_form=forms.MusicianForm()
    dict={
        "test_form":new_form,
    }
    if request.method=="POST":
        new_form=forms.MusicianForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            dict.update({'submitted':"Added Succesfully!"})
            
    return render(request,'first_app/addMusician.html',context=dict)

