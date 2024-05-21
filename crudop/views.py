from django.shortcuts import render
from . import forms
from first_app import models
# Create your views here.
def crudop(request):
    dict={
        'title':'CRUD operation',
    }
    return render(request,'crudop/crudop.html',context=dict)

def album_list(request,artist_id):
    artist_info=models.Album.objects.filter(artist=artist_id)
    musician_info=models.Musician.objects.get(pk=artist_id)
    dict={
        'artist_info':artist_info,
        'tittle': "Artist Info:",
        'musician_info':musician_info,
    }
    
    return render(request,'crudop/album_list.html',context=dict)

def add_musician(request):
    new_form=forms.add_musician_form()
    dict = {
        'title':'Add operatrion',
        'form': new_form,
    }
    
    if request.method=="POST":
        new_form=forms.add_musician_form(request.POST)
        dict.update({'form':new_form})
        
        if new_form.is_valid():
            new_form.save()
            dict.update({'form_submitted':'submitted'})
 
    return render(request,'crudop/add_musician.html',context=dict)

def musician_list(request):
    musicians = models.Musician.objects.all()
    print(musicians)
    dict = {
        'title':'Musician list',
        'musicians': musicians,
        }
    return render(request,'crudop/musician_list.html',context=dict)

def add_album(request):
    new_form=forms.add_album_form()
    dict = {
        'title':'Add operatrion',
        'form': new_form,
    }
    
    if request.method=="POST":
        new_form=forms.add_album_form(request.POST)
        dict.update({'form':new_form})
        
        if new_form.is_valid():
            new_form.save()
            dict.update({'form_submitted':'submitted'})
    return render(request,'crudop/add_album.html',context=dict)

def edit_artist_info(request,artist_id):
    artist_info=models.Musician.objects.get(pk=artist_id)
    new_form=forms.add_musician_form(instance=artist_info)
    if request.method=='POST':
        new_form=forms.add_musician_form(request.POST,instance=artist_info)
        if new_form.is_valid():
            new_form.save(commit=True)
            return album_list(request,artist_id)
    dict={
        'form': new_form,
    }
    return render(request,'crudop/edit_artist_info.html',context=dict)

def edit_album(request,album_id):
    album_info=models.Album.objects.get(pk=album_id)
    new_form=forms.add_album_form(instance=album_info)
    dict={
        'form': new_form,
    }
    if request.method=='POST':
        new_form=forms.add_album_form(request.POST,instance=album_info)
        if new_form.is_valid():
            new_form.save(commit=True)
            dict.update({'success':"Successfully Updated!"})
    dict.update({
        'form': new_form,
        'album_id':album_id,
    })
    return render(request,'crudop/edit_album.html',context=dict)

def delete_album(request,album_id):
    album=models.Album.objects.get(pk=album_id).delete()
    
    dict={
        "success":'Album Deleted Succesfully!'
    }
    return render(request,'crudop/delete.html',context=dict)