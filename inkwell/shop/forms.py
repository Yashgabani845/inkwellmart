from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer,Owner,Product


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'username', 'password1','password2']
    

