from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    return render(request,'accounts/home.html')

def register(request):
    return render(request,'accounts/register.html')

def login(request):
    if request.method=='POST':
        form=AuthenticationForm()
    else:
        form=AuthenticationForm()


    return render(request,'accounts/login.html',{form:'form'})

