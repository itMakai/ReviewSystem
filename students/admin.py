from django.contrib import admin
from students.models import Student, Lecturer, Review_detail

# Register your models here.
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Review_detail)