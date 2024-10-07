from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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
        
        
        
        # create Cutsomer Profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modfiied = models.DateTimeField(User, auto_now = True)
    phone = models.CharField(max_length = 20, blank = True)
    addess1 = models.CharField(max_length = 200, blank = True)
    addess2 = models.CharField(max_length = 200, blank = True)
    city = models.CharField(max_length = 200, blank = True)
    state = models.CharField(max_length = 200, blank = True)
    zipcode = models.CharField(max_length = 200, blank = True)
    country = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return self.user.username

 # Create a user Profile by Default when user signs up

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()

# Automate the profile thing

post_save.connect(create_profile, sender = User)



class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"