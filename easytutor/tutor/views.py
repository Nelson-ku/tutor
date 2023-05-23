from django.shortcuts import render, redirect

# Create your views here.

def login(request):

    return render(request,'tutor/login.html')

def register(request):

    return render(request,'tutor/register.html')

def tutorRegister(request):

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
