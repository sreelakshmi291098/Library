from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Stud_reg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    age=models.IntegerField()
    cource=models.CharField(max_length=500)
    gender=models.CharField(max_length=500)
    status=models.CharField(max_length=10)
    role=models.CharField(max_length=20)

class Teacher_reg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    age=models.IntegerField()
    cource=models.CharField(max_length=500)
    gender=models.CharField(max_length=500)
    status=models.CharField(max_length=10)
    role=models.CharField(max_length=20)

class Bookdetail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book_id=models.IntegerField()
    book_title=models.CharField(max_length=100)
    book_author=models.CharField(max_length=100)
    book_cost=models.CharField(max_length=100)
    status=models.CharField(max_length=10)

class fine(models.Model):
    book_title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    delay=models.IntegerField()
    ammount=models.IntegerField()
    
