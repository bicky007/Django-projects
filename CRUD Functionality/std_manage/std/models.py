from django.db import models

# Create your models here.

class Student(models.Model):
    roll=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)