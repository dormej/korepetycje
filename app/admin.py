from django.contrib import admin

from app.models import Teacher, Student, Exercise

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Exercise)
