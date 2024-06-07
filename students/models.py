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
    
    
    
class Review(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    date = models.DateField(default = timezone.now)
    
    def __str__(self):
        return self.review
    
    
class ReviewDetail(models.Model):
    studentName = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, related_name='review_details', on_delete=models.CASCADE)
    rating = models.ForeignKey(Review, on_delete=models.CASCADE)
    date_reviewed = models.DateTimeField(default=timezone.now)
