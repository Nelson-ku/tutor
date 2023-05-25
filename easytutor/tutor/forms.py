from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Student,Tutor


class StudentRegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=255)
    last_name=forms.CharField(max_length=255)

    class Meta:
        model=Student
        fields=('username','first_name','last_name','password1','password2')

class TutorRegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=255)
    last_name=forms.CharField(max_length=255)

    class Meta:
        model=Tutor
        fields=('username','first_name','last_name','password1','password2')

class LoginForm(AuthenticationForm):
    class Meta:
        fields=('email','password')
