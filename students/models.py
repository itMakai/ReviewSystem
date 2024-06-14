from datetime import timezone
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year_of_study = models.IntegerField()
    program = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    password= models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name}'
    
class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
class Review_detail(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    review_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Review for {self.lecturer.name} by {self.student.first_name} on {self.review_date}'
    
    
    
