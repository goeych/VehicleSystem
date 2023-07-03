from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

from generalExpense.models import Customer

class CreateCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields=['email','username','password1','password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
