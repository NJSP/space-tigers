from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
        # New field for the directory of the 3D model
    model_directory = models.CharField(max_length=255, blank=True, null=True)
    model_file_name = models.CharField(max_length=100, blank=True, null=True)

    

        