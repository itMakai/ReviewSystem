from datetime import timezone
from django.utils import timezone
from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(default=0000, max_length=100)
    department = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    course = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    
class Review_detail(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    review_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Review for {self.lecturer.name} by {self.student.name}'
    
    
    
