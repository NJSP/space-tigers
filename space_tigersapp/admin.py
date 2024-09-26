from django.contrib import admin
from .models import Product, Customer

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')

admin.site.register(Product)
admin.site.register(Customer)