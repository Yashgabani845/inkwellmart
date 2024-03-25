from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer,Owner,Product


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'username', 'password1','password2']
    

class OwnerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'sales']

    def clean_sales(self):
        sales = self.cleaned_data.get('sales')
        if sales < 0:
            raise forms.ValidationError("Sales value cannot be negative.")
        return sales
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if Owner.objects.filter(name=name).exists():
            raise forms.ValidationError("This name is already taken. Please choose another one.")
        return name