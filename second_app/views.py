from django.shortcuts import render
from second_app import forms
# Create your views here.
def second_app(request):
    new_form=forms.second_form()
    dict={
        "key1":"this is from second App",
        "form":new_form,
    }
    if request.method=='POST':
        new_form=forms.second_form(request.POST)
        if new_form.is_valid():
            user_name=new_form.cleaned_data['user_name']
            # boolean_field=new_form.boolean_field
            boolean_field=new_form.cleaned_data['boolean_field']
            dict.update({"user_name":user_name})
            dict.update({"boolean_field":boolean_field})
            dict.update({'form_submitted':"submitted!"})
    
    return render(request,'second_app/form.html',context=dict)

def form_validation_test(request):
    print(' form_validation initiated')
    new_form=forms.form_validation_test()
    print(new_form)
    dict={
        "form":new_form,
        'key1':'testing form validation using integer number',
    }
    
    if request.method=="POST":
        new_form=forms.form_validation_test(request.POST)
        #print(' if initiated')
        dict.update({'form':new_form})
        if new_form.is_valid():
            number=new_form.cleaned_data['numberField']
            dict.update({"numberField":number})
            dict.update({'form_submitted':"submitted!"})
    return render(request,'second_app/integervalidation.html',context=dict)

def emailVerification(request):
    new_form=forms.emailVerification()
    dict={
        "form":new_form,
        "key1":"email Verification!"
        }
    if request.method=="POST":
        new_form=forms.emailVerification(request.POST)
        dict.update({'form':new_form})
        if new_form.is_valid():
            email=new_form.cleaned_data['email']
            dict.update({'email':email})
            dict.update({"form_submitted":"submitted"})
    
    return render(request,'second_app/emailverifcation.html',context=dict)