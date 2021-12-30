from django.contrib import admin

from authentication.models import Student, Teacher

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
