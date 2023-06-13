from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import StudentRegistrationForm,TutorRegistrationForm,LoginForm
from django.contrib import messages
from .models import User

# Create your views here.


def login(request):
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try to authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)
            # Redirect the user to the appropriate page based on their role
            if user.role == User.Role.STUDENT:
                # Redirect to student dashboard
                return redirect('questions')
            elif user.role == User.Role.TUTOR:
                # Redirect to tutor dashboard
                return redirect('tutorland')
        else:
            # Authentication failed, show an error message
            messages.info(request, 'username or password is incorrect')

    context={'form':form}
    # If it's a GET request, render the login template
    return render(request, 'tutor/login.html',context)

# def login(request):
#     form=LoginForm()
#     if request.method=='POST':
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login(request,user)
#             return redirect('tutorland')# replaced by home
#         else:
#             form=LoginForm()
#     context={'form':form}
#     return render(request,'tutor/login.html',context)


#student registration
def register(request):
    form = StudentRegistrationForm()

    if request.method=='POST':
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()

            return redirect('login')#replace with student home
        else:
            form=StudentRegistrationForm()

    context={'form':form}
    return render(request,'tutor/register.html',context)

def tutorRegister(request):
    form = TutorRegistrationForm()

    if request.method=='POST':
        form=TutorRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()

            return redirect('login')
        else:
            form=TutorRegistrationForm()
    context={'form': form}
    return render(request,'tutor/reg-tutor.html',context)

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
