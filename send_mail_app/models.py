from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    age=models.IntegerField()
    
    def __str__(self):
        return self.name

    
class Customer(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)        
    location=models.CharField(max_length=100)    
    city=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name)
    

class EmailHistory(models.Model):
    email_from=models.EmailField()
    email_to=models.EmailField()
    
    STATUS_CHOICES = [
    ('Success', 'Success'),
    ('Failed', 'Failed'),
    ('Pending', 'Pending'),
    ]
    
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    # status=models.CharField(max_length=100)    
    dateTime= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status
    

