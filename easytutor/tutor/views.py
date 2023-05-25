from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import StudentRegistrationForm,TutorRegistrationForm,LoginForm



# Create your views here.

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')# replaced by home
        else:
            form=LoginForm()
    return render(request,'tutor/login.html')


#student registration
def register(request):
    if request.method=='POST':
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')# replace with student home
        else:
            form=StudentRegistrationForm()
    return render(request,'tutor/register.html')

def tutorRegister(request):
    if request.method=='POST':
        form=TutorRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
        else:
            form=TutorRegistrationForm()

    return render(request,'tutor/reg-tutor.html')

def tutorlanding(request):

    return render(request, 'tutor/tutorlanding.html')


def Tutorform(request):

    return render (request,'tutor/tutorform.html')

def question(request):

    return render (request, 'tutor/Questions.html')

def payments(request):

    return render (request, 'tutor/payment.html')

def dashboards(request):

    return render (request, 'tutor/dashboard.html')
