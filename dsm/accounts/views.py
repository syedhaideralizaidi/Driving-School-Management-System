from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as authLogin,logout
from .models import customer
from django import forms
# Create your views here.
from .forms import MyForm

from django import forms
from django import forms
# Create your views here.

def my_form(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()
    return render(request, 'accounts/register.html', {'form': form})

def home(request):
    entries = customer.objects.all()
    context = {"entries": entries}
    return render(request,'accounts/home.html',{})

def register(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "accounts/register.html", context)
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        form=myauthenticate(username=username,password=password)
        if form:
            #print('hellllllllllllldsjdbjad\n')
            #if form.is_active:
            authLogin(request,form)
            entries = customer.objects.all()
            #print(f"Username --> {request.user.customer_uuid}")
            context = {'foo': 'bar'}

            return render(request, 'accounts/MainPage.html',{})
        #else:
            #print(forms.ValidationError);
    else:
        form=AuthenticationForm()


    return render(request,'accounts/login.html',{form:'form'})

def myauthenticate( username=None, password=None):

    try:

        user = customer.objects.get(name=username)

            #  Check the password is the reverse of the username
        if check_password(password, user.password_en):
                # Yes? return the Django user object
            return user
        else:
                # No? return None - triggers default login failed
            return None
    except customer.DoesNotExist:
            # No user was found, return None - triggers default login failed
        return None

    # Required for your backend to work properly - unchanged in most scenarios
'''def get_user(self, user_id):
    try:
        return customer.objects.get(pk=user_id)
    except customer.DoesNotExist:
        return None'''

def check_password(password1,password2):
    if password2==password1:
        return True
    else:
        return False

def getCurrentUserName(request):
    return {request.user.name}