from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    dict={
        'key1':"I am learning Django. Here passing a value from views Function",
        
    }
    return render(request,'first_app/index.html',context=dict)
