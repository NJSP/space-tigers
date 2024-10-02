from django import forms
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password', 'first_name', 'last_name', 'mi', 'email', 'mobile', 'avatar_url']
# automatically make a new user using the information from the CustomerForm
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']