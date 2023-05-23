from django.urls import path

from django.contrib.auth import views as auth_views

from .import views

urlpatterns=[
    path('',views.login,name='login'),
    path('register/',views.register, name='register'),
    path('tutor-reg/',views.tutorRegister, name='tutor-reg'),
    path('tutorland',views.tutorlanding,name='tutorland'),
    path('tutorform/',views.Tutorform,name='tutorform'),
    path('questions',views.question,name='questions'),
    path('payment',views.payments,name='payment'),
    path('dashboard',views.dashboards,name='dashboard')
]


