from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'accounts/home.html')

def register(request):
    return render(request,'accounts/register.html')

def login(request):
    return HttpResponse('loginpage')

