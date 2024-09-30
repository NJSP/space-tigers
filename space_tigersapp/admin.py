from django.contrib import admin
from .models import Product, Customer

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'mi', 'email', 'phone', 'avatar_url')

admin.site.register(Product)
admin.site.register(Customer)