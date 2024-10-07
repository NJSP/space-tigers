from django.contrib import admin
from .models import Product, Customer, Profile, Order
from django.contrib.auth.models import User  # Import User model

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'mi', 'email', 'phone', 'avatar_url')

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)

# Profile and User info

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User) 
admin.site.register(User, UserAdmin) 