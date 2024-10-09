from django.db import models
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
        # New field for the directory of the 3D model
    model_directory = models.CharField(max_length=255, blank=True, null=True)
    model_file_name = models.CharField(max_length=100, blank=True, null=True)

    
class Customer(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mi = models.CharField(max_length=1)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    avatar_url = models.CharField(max_length=2083)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"