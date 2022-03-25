from django import forms
from .models import customer

# creating a form
'''class InputForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=13)
    password = forms.CharField(widget=forms.PasswordInput())'''
class MyForm(forms.ModelForm):
  class Meta:
    model = customer
    fields = ["name", "email","phone",'password_en']
    labels = {'name': "Name", "email": "Email","phone":"Phone","password_en":"Password"}