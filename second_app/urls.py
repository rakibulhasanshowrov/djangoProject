from django.urls import path

# Your URL patterns

from . import views

urlpatterns=[
    path('form/',views.second_app,name="second_app"),
    path('form_validation_test/',views.form_validation_test,name="form_validation_test"),
    path('emailVerification/',views.emailVerification,name="emailVerification"),
]
