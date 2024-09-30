from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fname', 'lname', 'mi', 'email', 'phone', 'avatar_url']
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'mi': 'Middle Initial',
            'email': 'Email',
            'phone': 'Phone Number',
            'avatar_url': 'Avatar URL'
        }