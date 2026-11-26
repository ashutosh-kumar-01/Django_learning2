from django.db import models
from django.db.models import OneToOneField

# Create your models here.

class Emp(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    salary = models.IntegerField()
    age = models.IntegerField()
    def __str__(self):
        return self.firstname
   
   
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.title     
    
    
class Blogpost(models.Model):
    title = models.CharField(max_length=50)
    post = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.title    
    
    
    
from django.contrib.auth.models import User
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)    