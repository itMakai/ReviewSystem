from django.contrib import admin
from students.models import Student, Lecturer, Review, ReviewDetail

# Register your models here.
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Review)
admin.site.register(ReviewDetail)