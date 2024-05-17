from django.urls import path

# Your URL patterns

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('form/',views.form,name="form"),
    path('addMusician/',views.addMusician,name="addMusician"),
    
]

