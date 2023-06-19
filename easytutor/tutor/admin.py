from django.contrib import admin
from .models import Tutor,Student,Question,Answer,User

# Register your models here.
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(User)
