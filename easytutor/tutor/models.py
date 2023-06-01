from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager


# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN='ADMIN','Admin'
        STUDENT='STUDENT','Student'
        TUTOR='TUTOR','Tutor'

    base_role=Role.ADMIN

    role= models.CharField(max_length=50,choices=Role.choices)

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)


class Student(User):

    base_role = User.Role.STUDENT

    student=StudentManager()


class TutorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TUTOR)


class Tutor(models.Model):

    base_role = User.Role.STUDENT

    student=StudentManager()



class Question(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default='pending')
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    answer = models.TextField()
    explanation=models.TextField()
    rating = models.IntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Transaction(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
