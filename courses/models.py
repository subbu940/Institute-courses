from django.db import models
from django.utils import timezone


class Course(models.Model):
    course_name = models.CharField(max_length=20)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tools = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')


