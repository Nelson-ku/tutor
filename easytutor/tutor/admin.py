from django.contrib import admin
from .models import Tutor,Student,Question,Answer,User

# Register your models here.
admin.register(Tutor)
admin.register(Student)
admin.register(Question)
admin.register(Answer)
admin.register(User)
